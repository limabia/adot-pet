# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from adot.forms import SignUpForm


def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('platform:home')
    else:
        signup_form = SignUpForm()

    return render(request, 'signup.html', {'signup_form': signup_form})


def signup_pet(request):
    return render(request, 'signup_pet.html')

def pets(request):
    return render(request, 'pets.html')