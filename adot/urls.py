# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views import View
from django.views.defaults import page_not_found
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # index
    url(r'^$', views.index, name="index"),

]
