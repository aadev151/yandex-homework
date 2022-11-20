from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        help_text='Оставьте здесь свой отзыв',
        verbose_name='Текст отзыва'
    )
    created_on = models.DateTimeField(auto_now_add=True)
