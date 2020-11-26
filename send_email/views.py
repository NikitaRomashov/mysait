from django.shortcuts import render
from django.http import HttpResponse
import django
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail, mail_managers
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def send(request):
    return render(request, 'send_email/index.html')


def success(request):
    email = request.POST['email_adress']
    #emailAdmin = 'nikitos1654@gmail.com'
    data = request.POST['email_massege']+"\nОтветить на этот email: "+email
    send_mail('Спасибо', 'Спасибо Вы отправили сообщение',email, [email], fail_silently=False)#сообщение получателю
    #send_mail('Не спи админ', data, email, [emailAdmin], fail_silently=False) #Сообщение людям указанным в emailadmin
    mail_managers('Вам в лицо письмецо', data)
    return HttpResponseRedirect(reverse('blog:about'))
