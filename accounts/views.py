from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
         messages.success(request, 'Вы успешно зарегистрировались')
         return HttpResponseRedirect(reverse('blog:home'))
      else:
         messages.error(request,'Ошибка регистрации')
   else: 
      form = UserRegisterForm()
   return render(request, 'accounts/register.html', {"form": form})


def user_login(request):
   if request.method == 'POST':
      form = UserLoginForm(data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
         return HttpResponseRedirect(reverse('blog:home'))
   else:
      form = UserLoginForm()
   return render(request, 'accounts/login.html', {"form": form})


def user_logout(request):
   logout(request)
   return HttpResponseRedirect(reverse('blog:home'))
