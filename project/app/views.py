from django.shortcuts import render
from .models import Postindex
from .functions.get_post_type import get_post_type

def index(request):
    return render(request, 'base.html')

def postindex(request):
    data=Postindex.objects.all()[5909:5910]
    for row in data:
        id = row.id
        post_index_value = row.post_index_value
        post_name =row.post_name
        post_type = get_post_type(row.post_type)
        post_sub = row.post_sub
        region = row.region
        autonomy = row.autonomy
        area = row.area
        city = row.city
        city_1 = row.city_1
        actual_date = row.actual_date
        index_old = row.index_old
    context={'db':data,
             'id':id,
             'post__index_value':post_index_value,
             'post_name': post_name,
             'post_type': post_type,
             'post_sub':post_sub,
             'region':region,
             'autonomy':autonomy,
             'area':area,
             'city':city,
             'city_1':city_1,
             'actual_date':actual_date,
             'index_old':index_old
             }
    return render(request, 'postindex.html', context)