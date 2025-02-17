from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from .tools import send_email_confirmation_registration
from django.shortcuts import redirect, reverse, render
from django.http import HttpResponseBadRequest
from django.db import IntegrityError
from smtplib import SMTPDataError
from .models import MinUser


def index(request):
    if not request.method in ['GET', 'POST']:
        return HttpResponseBadRequest(request)

    else:
        if request.method == 'GET':
            message = request.GET.get('message', '')

            return render(request, 'authentication/html/index.html', {'message': message})

        elif request.method == 'POST':
            message = ''

            if not request.POST.get('act', '') in ['login', 'registration']:
                message = 'Заполненная форма не соответствует ожиданию сервера'

            else:
                if 'login' == request.POST['act']:
                    email = request.POST['email']
                    password = request.POST['password']

                    user = authenticate(email=email, password=password)

                    if user is None:
                        message = 'Аккаунт не найден, либо не активирован'
                    else:
                        if user.is_blocked:
                            message = 'Аккаунт заблокирован'
                        else:
                            django_login(request, user)
                            return redirect(to='http://127.0.0.1:8000/chat/', permanent=True)

                elif 'registration' == request.POST['act']:
                    email = request.POST['email']
                    password = request.POST['password']

                    try:
                        user = MinUser.objects.create_user(email=email, password=password)
                        user.save()

                        if 'trust_registration' in request.POST:
                            message = f'Аккаунт создан без проверок, ваш UID = {user.uid}'

                        else:
                            message = 'Письмо с активацией отправлено на почту'
                            send_email_confirmation_registration(email)

                    except IntegrityError:
                        message = 'Аккаунт с такой почтой уже существует'

                    except SMTPDataError:
                        message = 'Ошибка отправки письма'

            return redirect(reverse('index_auth') + f'?message={message}', permanent=True)


def confirmation_registration(request, token):
    message = 'Аккаунт успешно активирован'

    try:
        user = MinUser.objects.get(email=token)

        if user.is_active:
            message = 'Аккаунт уже подтвержден'
        else:
            user.is_active = True
            user.save()

    except:
        message = 'Ошибка активации'

    return redirect(reverse('index_auth') + f'?message={message}', permanent=True)


@login_required
def logout(request):
    django_logout(request)
    return redirect(reverse('index_auth') + '?message=Вы вышли из аккаунта', permanent=True)