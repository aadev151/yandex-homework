from django.shortcuts import render

from catalog.models import Item


def home(request):
    context = {
        'items': (
            Item.objects.published()
            .filter(is_on_main=True)
            .order_by('name')
        ),
    }
    return render(request, 'homepage/index.html', context=context)
