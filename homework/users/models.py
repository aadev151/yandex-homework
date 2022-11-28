from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from users.managers import EmailUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True
    )
    birthday = models.DateField(
        verbose_name='День рождения',
        blank=True,
        null=True,
        validators=[MaxValueValidator(limit_value=date.today)]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = EmailUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
