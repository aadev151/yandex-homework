from django.core.mail import send_mail
from django.views.generic import FormView


from . import forms
from feedback.models import Feedback
from homework.settings import SENT_FROM_EMAIL, ADMIN_EMAIL


class FeedbackView(FormView):
    form_class = forms.FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/feedback/'

    def form_valid(self, form):
        feedback_text = form.cleaned_data['text']

        Feedback.objects.create(text=feedback_text)
        send_mail(
            'Вы отправили отзыв',
            f'Вы отправили следующий отзыв: {feedback_text}',
            SENT_FROM_EMAIL,
            [
                ADMIN_EMAIL,
            ],
        )
        return super().form_valid(form)
