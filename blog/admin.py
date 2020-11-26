from django.contrib import admin
from .models import Article, Comment, ArticleImage
from django.utils.safestring import mark_safe


class ArticleImageAdmin(admin.ModelAdmin):
    pass


# TabularInline - как в админке будет выводится
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    #max_num = 10
    #extra = 0
	 #Добваления поля которое нельзя редактировать
    fk_name = 'article'
    readonly_fields = ["preview"]
#Сам метод
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="100">')
        

    




class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline, ]

    



admin.site.register(Comment)
admin.site.register(ArticleImage, ArticleImageAdmin)
admin.site.register(Article, ArticleAdmin)


