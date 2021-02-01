# Generated by Django 3.1.2 on 2021-02-01 08:50

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimage',
            name='image',
            field=models.ImageField(upload_to='', validators=[blog.models.ArticleImage.validate_image], verbose_name='Фотографии статьи'),
        ),
    ]
