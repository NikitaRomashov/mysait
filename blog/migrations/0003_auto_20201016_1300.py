# Generated by Django 3.1.2 on 2020-10-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201016_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=200, verbose_name='Заголовок статьи'),
        ),
    ]
