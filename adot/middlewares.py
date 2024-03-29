from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

from adot.forms import LoginForm, SignUpForm


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # before each request
        if request.method == 'POST':
            login_form = LoginForm(request=request, data=request.POST, initial={})
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('pets')
        else:
            login_form = LoginForm()
        request.login_form = login_form

        # process request
        response = self.get_response(request)

        return response
