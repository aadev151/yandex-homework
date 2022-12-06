from django.views.generic import ListView

from catalog.models import Item


class HomeView(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.published().filter(is_on_main=True)
    template_name = 'homepage/index.html'
