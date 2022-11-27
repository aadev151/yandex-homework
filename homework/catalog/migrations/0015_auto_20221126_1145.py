# Generated by Django 3.2.4 on 2022-11-26 11:45

import catalog.validators
from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_alter_item_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=tinymce.models.HTMLField(help_text='Информация о товаре. Должна содержать слова "превосходно" или "роскошно"', validators=[catalog.validators.validate_must_be_param], verbose_name='Описание товара'),
        ),
    ]
