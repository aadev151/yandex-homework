from django.views.generic import ListView, DetailView

from catalog.models import Item


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.published_sorted_by_category()
    template_name = 'catalog/index.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    queryset = Item.objects.images()
    template_name = 'catalog/item.html'
