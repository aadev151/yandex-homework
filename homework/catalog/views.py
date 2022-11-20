from django.http import HttpResponseNotFound
from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    template = 'catalog/index.html'
    context = {
        'items': (
            Item.objects.published_sorted_by_category()
        ),
    }
    return render(request, template, context=context)


def item_detail(request, pk):
    template = 'catalog/item.html'

    item = Item.objects.images(pk)
    if not item:
        return HttpResponseNotFound("it's 404 lol :)")
    context = {
        'item': item,
    }

    return render(request, template, context=context)
