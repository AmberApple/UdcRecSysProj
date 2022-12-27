from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from udc_rec_sys.models import UserStash, Article

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserLoginForm()
    context = {
        'title': _('uv_login_title'),
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('uv_register_success_msg'))
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': _('uv_register_title'),
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
    context = {
        'title': _('uv_profile_title'),
        'form': form,
        'userstashes': UserStash.objects.filter(user=user).order_by('-created_timestamp'),
        'count_user_articles': Article.objects.filter(owner=user).count()
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('udc_rec_sys:index'))
