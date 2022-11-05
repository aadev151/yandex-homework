from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from Core.models import CommonDataAbstractModel, SlugAbstractModel
from .validators import validate_must_be_param, validate_weight


class Tag(CommonDataAbstractModel, SlugAbstractModel):
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Category(CommonDataAbstractModel, SlugAbstractModel):
    weight = models.PositiveSmallIntegerField(
        default=100,
        validators=[
            validate_weight
        ],
        help_text=('Вес категории. Должен находиться в пределах '
                   '[1, 32766]. По умолчанию 100.'),
        verbose_name='Вес'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Item(CommonDataAbstractModel):
    text = models.TextField(
        validators=[
            validate_must_be_param('превосходно', 'роскошно')
        ],
        help_text=('Информация о товаре. '
                   'Должна содержать слова "превосходно" или "роскошно"'),
        verbose_name='Описание товара'
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text=('К какой категории относится товар?'),
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(
        Tag,
        help_text='Теги к товару',
        verbose_name='Теги'
    )

    upload = models.ImageField(upload_to='uploads/%Y/%m')

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '400x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
