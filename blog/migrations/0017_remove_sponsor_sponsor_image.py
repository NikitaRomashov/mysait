# Generated by Django 3.1.2 on 2020-12-06 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_sponsorimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='sponsor_image',
        ),
    ]
