from catalog.models import Item
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, View
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
        item = get_object_or_404(Item, pk=pk)

        if not item:
            return HttpResponseNotFound("it's 404 lol :)")

        initial_data = {}

        try:
            initial_data['score'] = Rating.objects.get(
                user_id=request.user.id
            ).score
        except Rating.DoesNotExist:
            initial_data['score'] = None

        rating_form = RatingForm(
            request.POST or None,
            initial=initial_data,
        )

        rating_queryset = Rating.objects.filter(item=item, score__isnull=False)
        all_ratings = list(map(lambda rating: rating.score, rating_queryset))

        if len(all_ratings) != 0:
            average = sum(all_ratings) / len(all_ratings)
        else:
            average = '0.0'

        context = {
            'item': item,
            'rating_form': rating_form,
            'average': average,
            'total': len(all_ratings),
        }

        return render(request, template, context=context)

    def post(self, request, pk):
        rating_form = RatingForm(request.POST)

        if not rating_form.is_valid():
            return redirect('catalog:item', pk=pk)

        rating, _ = Rating.objects.get_or_create(
            item=get_object_or_404(Item, pk=pk),
            user=request.user,
        )

        rating.score = rating_form.cleaned_data['score']
        rating.save()

        return redirect(reverse('users:profile'))
