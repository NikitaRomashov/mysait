# Generated by Django 3.1.2 on 2021-04-04 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210323_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_instagram',
            field=models.TextField(blank=True, verbose_name='Полная ссылка на инстаграм'),
        ),
    ]