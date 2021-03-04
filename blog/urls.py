from django.urls import path, include
from .import views
from django.conf.urls import url
from django.views.generic import RedirectView

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('history', views.history, name='history'),
    path('search/', views.searchInArticles, name='search_in_articles'),
    path('post/<int:article_id>', views.ArticleDetailView, name='article-detail'),
    path('post/<int:article_id>/leave_comment',
         views.leave_comment, name='leave_comment'),
    path('sponsor/<int:sponsor_id>',
         views.SponsorDetailView, name='sponsor-detail'),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/blog/img/favicon.ico', permanent=True)),
    path('QLDuk6dyOFrh59b9pf6hJyPnN', views.guard, name='guard'),
    #path('email', include('send_email.urls')),
    # для поиска


]
