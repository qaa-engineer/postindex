from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Postindex
from .functions.get_post_type import get_post_type


def index(request):
    return render(request, 'base.html')


def post_list(request):
    """
    Вывод постов
    """
    # Поиск по базе
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Postindex.objects.filter(Q(post_index_value__icontains=search_query) |
                                         Q(post_name__icontains=search_query) |
                                         Q(area__icontains=search_query) |
                                         Q(region__icontains=search_query)
                                         )
    else:
        posts = Postindex.objects.all()[:900]

    # Количество постов на странице
    number_of_records_per_page = 1
    paginator = Paginator(posts, number_of_records_per_page)
    # Номер странцы пагинации по умолчанию
    number_of_records_deafult = 5
    page_number = request.GET.get('page', number_of_records_deafult)
    page = paginator.get_page(page_number)
    # Количество страниц пагинации
    is_paginated = page.has_other_pages()
    # Определяем страницы Назад и Вперед
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    # Вывод поста в соответствии с номером в get-запросе адреса страницы
    post = posts[:page.number]
    # Достаем поля из  БД
    for row in post:
        id = row.id
        post_index_value = row.post_index_value
        post_name = row.post_name
        post_type = get_post_type(row.post_type)
        post_sub = row.post_sub
        region = row.region
        autonomy = row.autonomy
        area = row.area
        city = row.city
        city_1 = row.city_1
        actual_date = row.actual_date
        index_old = row.index_old
    # Передаем в контекст данные из БД и полученые данные из функций выше
    context = {'db': post,
               'id': id,
               'post_index_value': post_index_value,
               'post_name': post_name,
               'post_type': post_type,
               'post_sub': post_sub,
               'region': region,
               'autonomy': autonomy,
               'area': area,
               'city': city,
               'city_1': city_1,
               'actual_date': actual_date,
               'index_old': index_old,
               'page_object': page,
               'is_paginated': is_paginated,
               'prev_url': prev_url,
               'next_url': next_url,
               'post': post,
               }
    return render(request, 'post-detail.html', context=context)
