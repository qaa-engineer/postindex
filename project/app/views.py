from django.shortcuts import render, redirect
from .models import Name, Postindex


# Create your views here.
def index(request):
    names_from_db=Name.objects.all()
    context_dict={'names_from_context':names_from_db}
    return render(request, 'index.html', context_dict)

def postindex(request):
    all_data=Postindex.objects.all()
    context_all_data={'db':all_data}
    return render(request, 'postindex.html', context_all_data)