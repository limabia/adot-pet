# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')

def signup(request):
    return render(request, 'signup.html')