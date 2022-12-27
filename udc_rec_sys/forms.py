from django import forms
from django.utils.translation import ugettext as _

from udc_rec_sys.models import Article


class ArticleUploadForm(forms.ModelForm):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input'
    }), required=True)

    class Meta:
        model = Article
        fields = ('file', )
