# Generated by Django 3.1.2 on 2020-12-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20201206_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='sponsor_image',
            field=models.ImageField(blank=True, upload_to='sponsors/', verbose_name='Логотип спонсора'),
        ),
    ]