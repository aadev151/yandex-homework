from django.test import Client, TestCase
from django.urls import reverse

from feedback.models import Feedback


class FeedbackFormTests(TestCase):
    def test_form_is_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_correct_labels_and_help_texts(self):
        response = Client().get(reverse('feedback:feedback'))
        form = response.context['form']
        text_field = form.fields[Feedback.text.field.name]
        self.assertEquals(text_field.label, 'Текст отзыва')       
        self.assertEquals(text_field.help_text, 'Оставьте здесь свой отзыв')

    def test_redirect_after_filling_form(self):
        form_data = {
            'text': 'Тестовый отзыв',
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follows=True
        )
        self.assertRedirects(response, reverse('feedback:feedback'))
