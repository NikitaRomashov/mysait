from django.contrib import admin
from .models import Article, Comment, ArticleImage, Sponsor, SponsorImage, Contact
from django.utils.safestring import mark_safe


class ArticleImageAdmin(admin.ModelAdmin):
    pass


# TabularInline - как в админке будет выводится
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    #max_num = 10
    #extra = 0
    # Добваления поля которое нельзя редактировать
    fk_name = 'article'
    readonly_fields = ["preview"]
# Сам метод

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="100">')


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleImageInline, ]


class SponsorImageAdmin(admin.ModelAdmin):
    pass


# TabularInline - как в админке будет выводится
class SponsorImageInline(admin.TabularInline):
    model = SponsorImage
    max_num = 1
    #extra = 0
    # Добваления поля которое нельзя редактировать
    fk_name = 'sponsor'
    readonly_fields = ["preview"]
# Сам метод

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="100">')


class SponsorAdmin(admin.ModelAdmin):
    inlines = [SponsorImageInline, ]


admin.site.register(Comment)
admin.site.register(ArticleImage, ArticleImageAdmin)
admin.site.register(Article, ArticleAdmin)


admin.site.register(SponsorImage, SponsorImageAdmin)
admin.site.register(Sponsor, SponsorAdmin)


admin.site.register(Contact)
