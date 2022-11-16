from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    context = {
        'items': (
            Item.objects.published()
            .order_by('category__name')
        ),
    }
    return render(request, 'catalog/index.html', context=context)


def item_detail(request, pk):
    context = {
        'item': get_object_or_404(Item, id=pk)
    }

    return render(request, 'catalog/item.html', context=context)


def item_gallery(request, pk):
    context = {
        'item': Item.objects.images(pk)
    }
    return render(request, 'catalog/item_image_gallery.html', context=context)
