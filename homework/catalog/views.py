from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

from catalog.models import Item
from rating.forms import RatingForm
from rating.models import Rating


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

    initial_data = {}
    try:
        initial_data['score'] = Rating.objects.get(
            user_id=request.user.id).score
    except Rating.DoesNotExist:
        initial_data['score'] = None

    rating_form = RatingForm(
        request.POST or None,
        initial=initial_data,
    )

    if request.method == 'POST' and rating_form.is_valid():
        rating, _ = Rating.objects.get_or_create(
            item=item,
            user=request.user,
        )

        rating.score = rating_form.cleaned_data['score']
        rating.save()

        return redirect(reverse('users:profile'))

    try:
        rating_queryset = Rating.objects.filter(item=item, score__isnull=False)
        all_ratings = list(map(lambda rating: rating.score, rating_queryset))
        average = sum(all_ratings) / len(all_ratings)
    except ZeroDivisionError:
        average = float(0)

    context = {
        'item': item,
        'rating_form': rating_form,
        'average': average,
        'total': len(all_ratings),
    }

    return render(request, template, context=context)
