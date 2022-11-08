from django.db import models
from sorl.thumbnail import get_thumbnail


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


class ImageAbstractModel(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Название изображения. Максимально 150 символов',
        verbose_name='Название изображения'
    )
    upload = models.ImageField(
        upload_to='uploads/%Y/%m',
        verbose_name='Изображение'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    class Meta:
        abstract = True
