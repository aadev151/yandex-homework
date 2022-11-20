from django.core.mail import send_mail
from django.shortcuts import redirect, render

from . import forms
from feedback.models import Feedback


def feedback(request):
    template = 'feedback/feedback.html'

    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        feedback_text = form.cleaned_data['text']
        send_mail(
            'Вы отправили отзыв',
            'Вы отправили следующий отзыв:\n'
            f'{feedback_text}',
            'from@kittysneakers.example-domain',
            ['to@kittysneakers.example-domain']
        )
        Feedback.objects.create(
            text=feedback_text
        )

        return redirect('feedback:feedback')

    return render(request, template, context=context)
