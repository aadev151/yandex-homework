# Generated by Django 3.2.4 on 2022-11-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.IntegerField(help_text='Оставьте здесь свой отзыв', verbose_name='Текст отзыва')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
