# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # index
    path('', views.index, name="index"),
    path('cadastro', views.signup, name="cadastro"),
    path('cadastro-pet', views.signup_pet, name="cadastro-pet"),
    path('logout', views.logout, name="logout"),
    path('platform', include('plataform.urls', namespace='platform')),
]
