from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    username = forms.EmailField(label="Email:", help_text='Informe um endereço de e-mail válido.')
    password = forms.CharField(label="Escolha uma senha:", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Repita a senha:", widget=forms.PasswordInput, help_text='As senhas inseridas devem ser iguais')
    birthdate = forms.DateField(label="Data de Nascimento", widget=forms.SelectDateWidget)
    telephone = PhoneNumberField(label="Celular:")
    terms_agree = forms.BooleanField(label="Li e aceito os termos de uso")
