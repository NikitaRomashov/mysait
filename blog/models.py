import datetime

from django.db import models
from django.utils import timezone
from django.db.models import ImageField
from django.core.exceptions import ValidationError
from PIL import Image, ImageEnhance

# Create your models here.


def add_watermark(image, watermark, opacity=1, wm_interval=0):

    assert opacity >= 0 and opacity <= 1
    if opacity < 1:
        if watermark.mode != 'RGBA':
            watermark = watermark.convert('RGBA')
        else:
            watermark = watermark.copy()
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
    layer = Image.new('RGBA', image.size, (0, 0, 0, 0))
    for y in range(0, image.size[1], watermark.size[1]+wm_interval):
        for x in range(0, image.size[0], watermark.size[0]+wm_interval):
            layer.paste(watermark, (x, y))
    return Image.composite(layer,  image,  layer)


if __name__ == "__main__":
    img = Image.open("asd.jpg")
    watermark = Image.open("watermark.png")

    result = add_watermark(img, watermark)
    result.save('result.png')


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
    #image = models.ImageField('Фотографии статьи')
    article = models.ForeignKey(
        Article, related_name="images", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фотография статьи'
        verbose_name_plural = 'Фотографии статьи'

    def __str__(self):
        return self.image.url

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла %sMB" %
                                  str(megabyte_limit))
    image = models.ImageField('Фотографии статьи', validators=[
                              validate_image])


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


class Sponsor(models.Model):
    sponsor_title = models.CharField('Название спонсора', max_length=200)
    sponsor_text = models.TextField('Описание')
    sponsor_link = models.TextField('Ссылка на сайт')

    def __str__(self):
        return self.sponsor_title

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Спонсор'
        verbose_name_plural = 'Спонсоры'


class SponsorImage(models.Model):
    #image = models.ImageField('Логотип спонсора')
    sponsor = models.ForeignKey(
        Sponsor, related_name="images", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Логотип спонсора'
        verbose_name_plural = 'Логотипы спонсора'

    def __str__(self):
        return self.image.url

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 0.5
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("Максимальный размер файла %sMB" %
                                  str(megabyte_limit))

    image = models.ImageField('Логотип спонсора', validators=[validate_image])


class Contact(models.Model):

    contact_adress = models.TextField('Адреса')
    contact_email = models.TextField('Email')
    contact_phone = models.TextField('Телефон')
    contact_instagram = models.TextField('Полная ссылка на инстаграм')

    def __str__(self):
        return self.contact_adress

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
