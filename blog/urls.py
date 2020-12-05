from django.urls import path, include
from .import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'), 
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('search/', views.searchInArticles, name='search_in_articles'),
    path('post/<int:article_id>', views.ArticleDetailView, name='article-detail'),
    path('post/<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
    #path('email', include('send_email.urls')),
	 #для поиска 
    

]


