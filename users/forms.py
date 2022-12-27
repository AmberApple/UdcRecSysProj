from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext as _

from users.models import User

default_widget_class = 'form-control py-4'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('uf_login_form_placeholder_username')
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': _('uf_login_form_placeholder_password')
    }))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = default_widget_class


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_first_name')
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_last_name')
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_username')
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_email')
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_password1')
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': _('uf_registration_form_placeholder_password2')
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = default_widget_class


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'company', 'position')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = default_widget_class
