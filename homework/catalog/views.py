from django.db.models import Avg, Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, View

from catalog.models import Item
from rating.forms import RatingForm
from rating.models import Rating


class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.published_sorted_by_category()
    template_name = 'catalog/index.html'


class ItemDetailView(View):
    def get(self, request, pk):
        template = 'catalog/item.html'
        item = get_object_or_404(Item.objects.images(), pk=pk)

        ratings = item.rating.aggregate(
            avg=Avg('score'),
            total=Count('score')
        )

        context = {
            'item': item,
            'average': ratings['avg'] or '0.0',
            'total': ratings['total'],
        }

        if request.user.is_authenticated:
            initial_data = {}
            try:
                initial_data['score'] = item.rating.get(
                    user__id=request.user.id
                ).score
            except Rating.DoesNotExist:
                initial_data['score'] = None

            rating_form = RatingForm(
                initial=initial_data,
            )

            context['rating_form'] = rating_form

        return render(request, template, context=context)

    def post(self, request, pk):
        rating_form = RatingForm(request.POST)

        if not rating_form.is_valid():
            return redirect('catalog:item', pk=pk)

        rating, _ = Rating.objects.get_or_create(
            item=get_object_or_404(Item, pk=pk),
            user=request.user,
        )

        new_score = rating_form.cleaned_data['score']
        if new_score:
            rating.score = new_score
            rating.save()
        else:
            rating.delete()

        return redirect(reverse('users:profile'))
