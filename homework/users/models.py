from datetime import date

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )

    birthday = models.DateField(
        help_text='День рождения пользователя',
        verbose_name='День рождения',
        null=True,
        blank=True,
        validators=[MaxValueValidator(limit_value=date.today)]
    )

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return f'День рождения для пользователя {self.user.username}'
