from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

from Core.models import (CommonDataAbstractModel,
                         SlugAbstractModel, ImageAbstractModel)
from .validators import validate_must_be_param, validate_weight


class Tag(CommonDataAbstractModel, SlugAbstractModel):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

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
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Item(CommonDataAbstractModel):
    text = HTMLField(
        validators=[
            validate_must_be_param('превосходно', 'роскошно')
        ],
        help_text=('Информация о товаре. '
                   'Должна содержать слова "превосходно" или "роскошно"'),
        verbose_name='Описание товара',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text='К какой категории относится товар?',
        verbose_name='Категория'
    )
    tags = models.ManyToManyField(
        Tag,
        help_text='Теги к товару',
        verbose_name='Теги'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name

    def image_tmb(self):
        if self.main_image.upload:
            return mark_safe(
                f'<img src="{self.main_image.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Image(ImageAbstractModel):
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        related_name='main_image'
    )

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'

    def __str__(self):
        return self.name


class Gallery(ImageAbstractModel):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    class Meta:
        verbose_name = 'изображение для галереи'
        verbose_name_plural = 'изображения для галереи'

    def __str__(self):
        return self.name

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True
