# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'platform'
urlpatterns = [
    path('', views.home, name="home"),
]
