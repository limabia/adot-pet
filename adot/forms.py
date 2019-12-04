from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from phonenumber_field.formfields import PhoneNumberField
from django.utils.safestring import mark_safe


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    username = forms.EmailField(label="Email:", help_text='Informe um endereço de e-mail válido.')
    password1 = forms.CharField(label="Escolha uma senha:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita a senha:", widget=forms.PasswordInput, help_text='As senhas inseridas devem ser iguais')
    birthdate = forms.DateField(
        label="Data de Nascimento",
        widget=forms.SelectDateWidget(
            years=range(timezone.now().year-100, timezone.now().year+1)
        ),
        initial=timezone.now().date()
    )
    telephone = PhoneNumberField(label="Celular:")
    terms_agree = forms.BooleanField(label=mark_safe('Li e aceito os <a href="#" target="_blank">termos de uso</a>'))
