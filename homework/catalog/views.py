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

    all_ratings = (item.rating.filter(score__isnull=False)
                   .values_list('score', flat=True))
    print(all_ratings, type(all_ratings))
    if len(all_ratings) != 0:
        average = sum(all_ratings) / len(all_ratings)
    else:
        average = '0.0'

    context = {
        'item': item,
        'average': average,
        'total': len(all_ratings),
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
            request.POST or None,
            initial=initial_data,
        )

        context['rating_form'] = rating_form

        if request.method == 'POST' and rating_form.is_valid():
            rating, _ = Rating.objects.get_or_create(
                item=item,
                user=request.user,
            )

            rating.score = rating_form.cleaned_data['score']
            rating.save()

            return redirect(reverse('users:profile'))

    return render(request, template, context=context)
