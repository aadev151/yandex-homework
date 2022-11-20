from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = 'homepage/index.html'
    context = {
        'items': (
            Item.objects.published()
            .filter(is_on_main=True)
        ),
    }

    return render(request, template, context=context)
