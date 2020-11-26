# Generated by Django 3.1.2 on 2020-10-13 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Заголовок статьи')),
                ('article_text', models.TextField(verbose_name='Текст статьи')),
                ('article_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': '1Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_autor', models.CharField(max_length=100, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=300, verbose_name='Текст комментария')),
                ('comment_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотографии статьи')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.article')),
            ],
            options={
                'verbose_name': 'Фотография статьи',
                'verbose_name_plural': 'Фотографии статьи',
            },
        ),
    ]
