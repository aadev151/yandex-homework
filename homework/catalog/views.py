from django.http import HttpResponse
from django.shortcuts import render


def item_list(request):
    return render(request, 'catalog/index.html')


def item_detail(request, pk):
    if pk == 0:
        return HttpResponse('It should be a positive number', status=404)

    return render(request, 'catalog/item.html', {'item_number': pk})
