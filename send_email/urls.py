from django.urls import path
from .import views

app_name = 'send_email'
urlpatterns = [
    path('', views.send, name='send'),
    path('success', views.success, name='success'),

]
