# Generated by Django 3.1.2 on 2020-11-28 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201016_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_autor',
        ),
    ]
