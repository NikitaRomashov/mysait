# Generated by Django 3.1.2 on 2020-12-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201205_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_image',
            field=models.ImageField(upload_to='', verbose_name='Логотип спонсора'),
        ),
    ]