# Generated by Django 3.1.2 on 2021-02-01 08:52

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210201_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorimage',
            name='image',
            field=models.ImageField(upload_to='', validators=[blog.models.SponsorImage.validate_image], verbose_name='Логотип спонсора'),
        ),
    ]