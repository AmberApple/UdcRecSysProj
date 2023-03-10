from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from udc_rec_sys.forms import ArticleUploadForm
from udc_rec_sys.models import Article, UserStash, ResourceDownload, ArticleStatus

from udc_rec_sys.tasks import assign_udc_code


# Create your views here.


def index(request):
    context = {
        'title': _('ursv_index_title')
    }
    return render(request, 'udc_rec_sys/index.html', context)


@login_required
def article_upload(request):
    if request.method == 'POST':
        form = ArticleUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            resourse_id = ResourceDownload(id=1)  # User Download
            status = ArticleStatus(id=1)  # Uploaded
            article = Article(file=request.FILES['file'], file_name=request.FILES['file'].name,
                              owner=request.user, resource=resourse_id, status=status)
            article.save()
            UserStash.objects.create(user=request.user, article=article)

            # start task
            #assign_udc_code.delay(pdf_file=str(article.file))
            assign_udc_code.apply_async(args=[str(article.file)], queue='assign_code')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ArticleUploadForm()
    context = {
        'title': _('ursv_article_upload_title'),
        'form': form
    }
    return render(request, 'udc_rec_sys/article_upload.html', context)
