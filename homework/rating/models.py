from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalog.models import Item
from users.models import User


class Rating(models.Model):
    SCORE_CHOICES = [
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь')
    ]
    score = models.PositiveSmallIntegerField(
        choices=SCORE_CHOICES,
        verbose_name='Оценка. От 1 до 5, где 1 - "ненависть", 5 - "любовь"',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True,
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='rating'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        unique_together = ('user', 'item')
