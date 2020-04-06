from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    #url('data/', views.data, name='data'),
    url('', views.index, name='index'),
]
