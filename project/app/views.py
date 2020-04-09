from django.shortcuts import render, redirect
from .models import Postindex

def index(request):
    return render(request, 'index.html')

def postindex(request):
    data=Postindex.objects.all()[5909:5910]
    context={'db':data}
    return render(request, 'postindex.html', context)