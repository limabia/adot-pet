from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)
