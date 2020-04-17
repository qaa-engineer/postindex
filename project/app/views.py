from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from .models import Postindex
from .functions.get_post_type import get_post_type
from django.template import RequestContext
from django.http import Http404
from django.urls import reverse


def home(request):
    return render(request, 'base.html')


#
# def post_list(request):
#     """
#     Вывод постов
#     """
#     search_query = request.GET.get('search', '')
#     if search_query:
#         posts = Postindex.objects.filter(Q(post_index_value__icontains=search_query) |
#                                          Q(post_name__icontains=search_query) |
#                                          Q(area__icontains=search_query) |
#                                          Q(region__icontains=search_query)
#                                          )
#     else:
#         posts = Postindex.objects.all()
#     # Количество постов на странице
#     number_of_records_per_page = 3
#     paginator = Paginator(posts, number_of_records_per_page)
#     # Номер странцы пагинации по умолчанию
#     number_of_records_deafult = 5
#     # Адрес страницы. 'page' - это параметр в URL
#     page_number = request.GET.get('page', number_of_records_deafult)
#     # Возвращаем страницу
#     page = paginator.get_page(page_number)
#     # Определяем, есть ли страницы для пагинации, нужна ли пагинация
#     is_paginated = page.has_other_pages()
#     # Определяем номера страниц Назад и Вперед
#     if page.has_previous():
#         prev_url = '?page={}'.format(page.previous_page_number())
#     else:
#         prev_url = ''
#     if page.has_next():
#         next_url = '?page={}'.format(page.next_page_number())
#     else:
#         next_url = ''
#     # Вывод поста в соответствии с номером в get-запросе адреса страницы
#     post = posts[:page.number]
#     # Достаем поля из  БД
#     for row in posts:
#         id = row.id
#         post_index_value = row.post_index_value
#         post_name = row.post_name
#         post_type = get_post_type(row.post_type)
#         post_sub = row.post_sub
#         region = row.region
#         autonomy = row.autonomy
#         area = row.area
#         city = row.city
#         city_1 = row.city_1
#         actual_date = row.actual_date
#         index_old = row.index_old
#     # Передаем в контекст данные из БД и полученые данные из функций выше
#     context = {'db': post,
#                'id': id,
#                'post_index_value': post_index_value,
#                'post_name': post_name,
#                'post_type': post_type,
#                'post_sub': post_sub,
#                'region': region,
#                'autonomy': autonomy,
#                'area': area,
#                'city': city,
#                'city_1': city_1,
#                'actual_date': actual_date,
#                'index_old': index_old,
#                'page_object': page,
#                'is_paginated': is_paginated,
#                'prev_url': prev_url,
#                'next_url': next_url,
#                'post': post,
#                }
#     return render(request, '21212.html', context=context)


def post_list(request):
    # Вывод всех данных из таблицы БД, равнозначно запросу SELECT * FROM public.postindex
    posts = Postindex.objects.all()
    # Создаем объект класса пагинации, второй параметр - это количество постов на каждой странице
    paginator = Paginator(posts, 10)
    # page - это posts, то есть вся БД, разделенная на страницы пагинации
    # Анализируем URL, достаем номер страницы пагинации из параметра ?page=10 и отдаем данные для этой страницы
    # Второй параметр в функции GET.get() - номер выбранной страницы по умолчанию, например, 1 - это начальная страница
    pages = paginator.get_page(request.GET.get('page', 1))
    ###########################################################
    # Вывод формы пагинации
    ###########################################################

    # Определяем существование страниц для пагинации
    is_paginated = pages.has_other_pages()

    # Определяем номера страниц Назад и Вперед для передачи их в context
    if pages.has_previous():
        prev_url = '?page={}'.format(pages.previous_page_number())
    else:
        prev_url = ''
    if pages.has_next():
        next_url = '?page={}'.format(pages.next_page_number())
    else:
        next_url = ''
    ###########################################################
    context = {'pages': pages,
               'is_paginated': is_paginated,
               'prev_url': prev_url,
               'next_url': next_url}
    return render(request, 'post-list.html', context)


def post_detail(request, slug):
    # Вывод всех данных из таблицы БД, равнозначно запросу SELECT * FROM public.postindex
    post = Postindex.objects.get(post_index_value__iexact=slug)

    id = post.id
    post_index_value = post.post_index_value
    post_name = post.post_name
    post_type = get_post_type(post.post_type)
    post_sub = post.post_sub
    region = post.region
    autonomy = post.autonomy
    area = post.area
    city = post.city
    city_1 = post.city_1
    actual_date = post.actual_date
    index_old = post.index_old

    context = {'post': post,
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
               }
    return render(request, 'post-detail.html', context)
