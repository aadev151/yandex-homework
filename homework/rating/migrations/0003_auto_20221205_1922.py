# Generated by Django 3.2.4 on 2022-12-05 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20221205_1858'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Оценка', 'verbose_name_plural': 'Оценки'},
        ),
        migrations.RemoveConstraint(
            model_name='rating',
            name='only_one_score',
        ),
    ]
