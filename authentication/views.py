from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import logout as django_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User


def index(request):
    return redirect(to='login', permanent=True)

def login(request):
    if request.method == 'GET':
        return render(request, 'authentication/html/index.html', {'is_login': True})

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email)

        if user is None:
            pass

    else:
        return HttpResponseBadRequest(request)

def registration(request):
    if request.method == 'GET':
        return render(request, 'authentication/html/index.html', {'is_login': False})

    elif request.method == 'POST':
        pass

    else:
        return HttpResponseBadRequest(request)

def register_confirm(request):
    pass

@login_required
def logout(request):
    django_logout(request)
    return redirect(to='login', permanent=True)