from django.db import models


class CommonDataAbstractModel(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Название. Максимальная длина - 150 символов',
        verbose_name='Название'
    )
    is_published = models.BooleanField(
        default=True,
        help_text='Показывает, видна ли запись на сайте (по умолчанию ДА)',
        verbose_name='Опубликовано?'
    )

    class Meta:
        abstract = True


class SlugAbstractModel(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text=('Уникальный идентификатор. '
                   'Максимальная длина - 200 символов. '
                   'Может содержать только латинские буквы, цифры, '
                   'дефис и нижнее подчеркивание (- и _). '
                   'Пример: My-Very-First-Model-1'),
        verbose_name='Slug'
    )

    class Meta:
        abstract = True
