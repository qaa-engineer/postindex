from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('postindex/', include([path('', views.post_list),
                                ])),
]
