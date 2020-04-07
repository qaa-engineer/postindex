from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('postindex/', views.postindex, name='postindex'),
    url('/', views.index, name='index'),
]
