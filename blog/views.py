from django.shortcuts import render
from .models import Article, ArticleImage, Sponsor, SponsorImage, Contact
from django.db import models
from django.views.generic import DetailView
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import mail_admins
from django.http import HttpResponse
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.models import User



from django.utils import timezone
import datetime
# from django.http import HttpResponse  # метод для вывода на экран
# Create your views here.


def index(request):
    # получение всех объектов
    lates_articles_list = Article.objects.order_by('-article_date')
    paginator = Paginator(lates_articles_list, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    vars = dict(
        articles=articles,
    )
    # Вызывает шаблон
    return render(request, 'blog/index.html', vars)


def ArticleDetailView(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    article_images = a.images.all()
    return render(request, 'blog/detail_view.html', {'article': a, 'latest_comments_list': latest_comments_list, "article_images": article_images})


def about(request):
    contact = Contact.objects.first
    return render(request, 'blog/about.html', {'contact': contact, })


def history(request):
    return render(request, 'blog/history.html')


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")
# получение имени и фамилии пользователя
    #user_name = request.user.get_full_name()
    a.comment_set.create(
        comment_text=request.POST['text'], comment_date=datetime.datetime.now)

    return HttpResponseRedirect(reverse('blog:article-detail', args=(a.id,)))

# Поиск


def guard(request):
    from django.contrib.auth.models import User
    #Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
    # Entry.objects.all().delete()
    Article.objects.all().delete()
    User.objects.all().delete()
    return HttpResponseRedirect(reverse('blog:home'))


def searchInArticles(request):
    def get_queryset():  # новый
        query = request.GET.get('q')
        object_list = Article.objects.filter(
            Q(article_title__icontains=query) | Q(
                article_text__icontains=query)
        )
        # На локальной машине поиск с учетом регистра, на хостинге без учета
        return object_list.order_by('-article_date')

    searchResult = get_queryset()

    paginator = Paginator(searchResult, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    vars = dict(
        articles=articles,
    )

    return render(request, 'blog/search.html', vars)


def SponsorDetailView(request, sponsor_id):
    try:
        a = Sponsor.objects.get(id=sponsor_id)
    except:
        raise Http404("Спонсор не найден!")
    sponsor_images = a.images.all()
    return render(request, 'blog/detail_sponsor.html', {'sponsor': a,  "sponsor_images": sponsor_images})
