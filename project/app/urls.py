from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('postindex/', post_list, name='post_list_url'),
    path('postindex/<slug>/', post_detail, name='post_detail_url'),
]
