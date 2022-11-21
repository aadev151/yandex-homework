from django.test import Client, TestCase
from django.urls import reverse

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_form_is_in_context(self):
        response = Client().get(reverse('feedback:feedback'))
        self.assertIn('form', response.context)

    def test_correct_labels_and_help_texts(self):
        text_field = self.form.fields[Feedback.text.field.name]
        self.assertEquals(text_field.label, 'Текст отзыва')
        self.assertEquals(text_field.help_text, 'Оставьте здесь свой отзыв')

    def test_redirect_and_creating_database_record_after_submitting_form(self):
        feedback_count = Feedback.objects.count()

        form_data = {
            'text': 'Тестовый отзыв',
        }
        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follows=True
        )

        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEquals(Feedback.objects.count(), feedback_count + 1)
        self.assertTrue(
            Feedback.objects.filter(
                text=form_data['text']
            ).exists()
        )
