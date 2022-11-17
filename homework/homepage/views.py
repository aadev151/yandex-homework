from django.shortcuts import render

from catalog.models import Item


def home(request):
    context = {
        'items': (
            Item.objects.published()
            .filter(is_on_main=True)
        ),
    }
    return render(request, 'homepage/index.html', context=context)
