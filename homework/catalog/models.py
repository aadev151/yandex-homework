from django.db import models

from .core_models import CommonDataAbstractModel, SlugAbstractModel
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
            validate_weight,
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
                   'Должна содержать слова \'превосходно\' или \'роскошно\''),
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

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
