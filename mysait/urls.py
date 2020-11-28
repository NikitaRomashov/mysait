from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Переходим в файл блог urls
    # для того чтобы вызвать функцию из другого приложения и не дать перейти на него
    path('', include('send_email.urls')),
    # path('accounts/', include('accounts.urls')),
    path('', include('social_django.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''if settings.DEGUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
