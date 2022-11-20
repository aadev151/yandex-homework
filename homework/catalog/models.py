from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

from Core.models import (CommonDataAbstractModel,
                         SlugAbstractModel, ImageAbstractModel)
from catalog.validators import validate_must_be_param, validate_weight


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


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .order_by('name')
                .select_related('category')
                .select_related('main_image')
                .prefetch_related(
                    models.Prefetch(
                        'tags',
                        queryset=Tag.objects.filter(is_published=True)
                    ))
        )

    def published_sorted_by_category(self):
        return self.published().order_by('category__name', 'name')

    def images(self, pk):
        return (
            self.get_queryset()
                .select_related('main_image')
                .prefetch_related('gallery')
                .filter(id=pk)
                .first()
        )


class Item(CommonDataAbstractModel):
    objects = ItemManager()

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

    is_on_main = models.BooleanField(
        default=False,
        help_text=(
            'Показывает, отображается ли товар на главной странице. '
            'По умолчанию НЕТ.'
        ),
        verbose_name='Отображается на главной странице?'
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)

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
