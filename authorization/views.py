from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from authorization.models import Tokens
from random import randint


def login(request):
    pass 

#registration
#https://www.youtube.com/watch?v=A8l-5I6x_6Y
def authorization(request):
    if request.method == 'GET':
        return HttpResponse('<html lang="en"><body>authorization GET</body></html>')
    
    elif request.method == 'POST':
        login = 'denkalmy@gmail.com'
        password = '123'

        user = authenticate(username="john", password="secret")

        if user is None:           
            token = Tokens(value=randint(100000, 999999), is_activate=False)
            token.save()

           send_mail(
            subject = "Подтверждение почты",
            message = f"Перейдите по ссылке, чтобы подтвердить регистрацию\nhttp://127.0.0.1:8000/auth/register_confirm/{token}",
            from_email = "dskm574@yandex.ru",
            recipient_list = [login, ],
            fail_silently=False
        )
    
        return HttpResponse('<html lang="en"><body>authorization GET</body></html>')



def register_confirm(request, token):
    if request == Tokens.objects.get(name=token):
        return HttpResponse('<html lang="en"><body>Успешная регистрация</body></html>')
