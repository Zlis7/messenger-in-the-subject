from smtplib import SMTPDataError
from django.db import IntegrityError
from django.shortcuts import redirect, reverse, render
from django.http import HttpResponseBadRequest
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .models import MinUser
import hashlib

def index(request):
    return redirect(reverse('login'), permanent=True)

def login(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return redirect(reverse('logout'), permanent=True)

        message = ''

        if 'message' in request.GET:
            message = request.GET['message']

        return render(request, 'authentication/html/index.html', {'is_login': True, 'message': message})

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        hash = hashlib.sha256()
        hash.update(bytes(email, 'utf-8'))

        user = authenticate(email=hash.hexdigest(), password=password)
        message = ''

        if user is not None:
            if not user.is_blocked:

                django_login(request, user)
                return redirect(to='http://127.0.0.1:8000/chat/', permanent=True)

            else:
                message = '?message=Аккаунт заблокирован'

        else:
            message = '?message=Аккаунт не найден, либо не активирован'

        return redirect(reverse('login') + message, permanent=True)

    else:
        return HttpResponseBadRequest(request)

def registration(request):
    if request.method == 'GET':

        if request.user.is_authenticated:
            return redirect(reverse('logout'), permanent=True)

        message = ''

        if 'message' in request.GET:
            message = request.GET['message']

        return render(request, 'authentication/html/index.html', {'is_login': False, 'message': message})

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        hash = hashlib.sha256()
        hash.update(bytes(email, 'utf-8'))

        try:
            user = MinUser(email=hash.hexdigest())
            user.set_password(password)
            user.save()

            if 'trust_registration' not in request.POST:
                pass
                #send_mail(
                 #       subject="Подтверждение почты",
                 #       message=f"Вы зарегистрировались в социальной сети «В теме».\nПерейдите по ссылке, чтобы подтвердить регистрацию, если вы не регистрировались не переходите по ссылке:\nhttp://127.0.0.1:8000/auth/register_confirm/{hash.hexdigest()}",
                 #       from_email="in.the.subject.574@yandex.ru",
                  #      recipient_list=(email,),
                  #      fail_silently=False
                #)

                return redirect(reverse('login') + '?message=Письмо с активацией отправлено на почту', permanent=True)

            return redirect(reverse('login') + '?message=Аккаунт создан', permanent=True)

        except IntegrityError:
            return redirect(reverse('login') + '?message=Аккаунт с такой почтой уже существует', permanent=True)

        except SMTPDataError:
            return redirect(reverse('login') + '?message=Ошибка отправки письма', permanent=True)

    else:
        return HttpResponseBadRequest(request)

def register_confirm(request, token):
    try:
        user = MinUser.objects.get(email=token)

        if user.is_active:
            return redirect(reverse('login') + '?message=Аккаунт уже подтвержден', permanent=True)

    except:
        return redirect(reverse('login') + '?message=Ошибка активации', permanent=True)

    user.is_active = True
    user.save()

    return redirect(reverse('login') + '?message=Вы прошли проверку', permanent=True)

@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse('login') + '?message=Вы вышли из аккаунта', permanent=True)