from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from authorization.models import Tokens
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import hashlib


def login(request):
    pass 

#registration
#https://www.youtube.com/watch?v=A8l-5I6x_6Y
@csrf_exempt
def authorization(request):
    if request.method == 'GET':
        return HttpResponse('<html lang="en"><body><form method="POST" action="/auth/regis"><button type="submit">POST</button></form></body></html>')
    
    elif request.method == 'POST':
        #user = authenticate(username="john", password="secret")

        #if user is None:  

        hash = hashlib.sha256()
        hash.update(b'denkalmy@gmail.com')

        user = User(
            username = 123, \
            email = hash.hexdigest(), \
            password = make_password('123'), \
            is_active = False)

        user.save()

        send_mail(\
            subject = "Подтверждение почты",\
            message = f"Перейдите по ссылке, чтобы подтвердить регистрацию\nhttp://127.0.0.1:8000/auth/register_confirm/{hash.hexdigest()}", \
            from_email = "dskm574@yandex.ru",\
            recipient_list = ('denkalmy@gmail.com', ),\
            fail_silently=False)
    
        return HttpResponse('<html lang="en"><body>authorization POST</body></html>')



def register_confirm(request, token):
    try:
        user = User.objects.get(email=token)

        if user.is_active:
            return HttpResponse('<html lang="en"><body>Пользователь уже активирован</body></html>')
    except:
        return HttpResponse('<html lang="en"><body>Токен не найден</body></html>')
    
    user.is_active = True
    user.save()

    return HttpResponse('<html lang="en"><body>Успешная регистрация</body></html>')

