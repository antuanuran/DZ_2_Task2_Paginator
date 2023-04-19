import csv

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

def first(request):

    with open('data.csv', 'r', encoding='utf-8') as fd:
        data = list(csv.DictReader(fd))
        leng = len(data)

    paginator = Paginator(data, 12)
    page_number = request.GET.get('page_name', 1)
    page_result = paginator.get_page(page_number)

    context = {
                    'all': page_result.object_list,
                    'page': page_result
              }

    return render(request, 'index_pag.html', context)
