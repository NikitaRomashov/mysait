import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    article_title = models.CharField('Заголовок статьи', max_length=200)
    article_text = models.TextField('Текст статьи')
    article_date = models.DateField('Дата публикации')
    #article_image = models.ImageField('Фотографии статьи')

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return ''

    def was_published_recently(self):
        return self.article_date >= (timezone.now().date() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = '1Статьи'


class ArticleImage(models.Model):
    image = models.ImageField('Фотографии статьи')
    article = models.ForeignKey(
        Article, related_name="images", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фотография статьи'
        verbose_name_plural = 'Фотографии статьи'

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #comment_autor = models.CharField('Имя автора', max_length=100)
    comment_text = models.CharField('Текст комментария', max_length=300)
    comment_date = models.DateTimeField('Дата комментария', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.comment_text
