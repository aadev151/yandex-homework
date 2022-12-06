# Generated by Django 3.2.4 on 2022-12-05 20:08

import catalog.validators
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0033_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=tinymce.models.HTMLField(help_text='Информация о товаре. Должна содержать слова "превосходно" или "роскошно"', validators=[catalog.validators.validate_must_be_param], verbose_name='Описание товара'),
        ),
    ]
