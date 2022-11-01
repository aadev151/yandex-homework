# Generated by Django 3.2 on 2022-11-01 19:55

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, help_text='Вес категории. Должен находиться в пределах [1, 32766]. По умолчанию 100.', validators=[catalog.validators.validate_weight], verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Информация о товаре. Должна содержать слова "превосходно" или "роскошно"', validators=[catalog.validators.validate_must_be_param], verbose_name='Описание товара'),
        ),
    ]
