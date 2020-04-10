from django.shortcuts import render
from .models import Postindex
from .functions.get_post_type import get_post_type

def index(request):
    return render(request, 'base.html')

def postindex(request):
    data=Postindex.objects.all()[5909:5910]
    for row in data:
        post_type=get_post_type(row.post_type)
    context={'db':data,
             'post_type':post_type}
    return render(request, 'postindex.html', context)