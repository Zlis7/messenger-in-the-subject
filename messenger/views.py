import hashlib
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, reverse
from .models import Chat

@login_required
def index(request):
    if request.method == 'GET':
        open_settings = 'off'

        if 'settings' in request.GET:
            if request.GET['settings'] == 'on':
                open_settings = 'on'
            else:
                return redirect(reverse('home-chat'), permanent=True)

        list_contacts = reversed(Chat.objects.filter(email_user = request.user.email))
        unique_list_contacts = []
        temp_id_chat = []

        for chat in list_contacts:
            if chat.id_chat not in temp_id_chat:
                unique_list_contacts.append(chat)
                temp_id_chat.append(chat.id_chat)

        context = {
            'main': 'off',
            'list_contacts': unique_list_contacts,
            'is_open_settings': open_settings,
            'user_name': request.user.username
        }

        return render(request, 'messenger/html/index.html', context)
    
    elif request.method == 'POST':
        if 'settings' in request.POST:
            if request.POST['settings'] == 'on':
                request.user.username = request.POST['username']
                request.user.save()

                return redirect(reverse('home-chat'), permanent=True)
    else:
        return HttpResponseBadRequest(request)


@login_required
def chat(request, id):
    if request.method == 'GET':
        list_contacts = Chat.objects.filter(id_chat = id).order_by("-date")

        context = {
            'main': 'on',
            'list_contacts': list_contacts,
            'id_chat': id,
            'email_user': request.user.email
        }

        return render(request, 'messenger/html/index.html', context)
    
    elif request.method == 'POST':
        pass
    else:
        return HttpResponseBadRequest(request)

