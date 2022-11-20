from django.core.mail import send_mail
from django.shortcuts import redirect, render

from . import forms


def feedback(request):
    template = 'feedback/feedback.html'

    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        send_mail(
            'Вы отправили отзыв',
            'Вы отправили следующий отзыв:\n'
            f'{form.cleaned_data["text"]}',
            'from@kittysneakers.example-domain',
            ['to@kittysneakers.example-domain']
        )
        return redirect('feedback:feedback')

    return render(request, template, context=context)
