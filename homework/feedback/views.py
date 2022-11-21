from django.core.mail import send_mail
from django.shortcuts import redirect, render

from . import forms
from feedback.models import Feedback
from homework.settings import SENT_FROM_EMAIL, ADMIN_EMAIL


def feedback(request):
    template = 'feedback/feedback.html'

    form = forms.FeedbackForm(request.POST or None)
    context = {
        'form': form,
    }

    if request.method == 'POST' and form.is_valid():
        feedback_text = form.cleaned_data['text']

        Feedback.objects.create(
            text=feedback_text
        )
        send_mail(
            'Вы отправили отзыв',
            f'Вы отправили следующий отзыв: {feedback_text}',
            SENT_FROM_EMAIL,
            [ADMIN_EMAIL, ]
        )

        return redirect('feedback:feedback')

    return render(request, template, context=context)
