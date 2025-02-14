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
                return redirect(reverse('chat'), permanent=True)

        list_contacts = Chat.objects.filter(email_user = request.user.email)
        unique_id_chats = []

        for i in list_contacts:
            if i.id_chat not in unique_id_chats:
                unique_id_chats.append(i.id_chat)

        list_contacts = []

        for i in unique_id_chats:
            objects = Chat.objects.filter(id_chat = i)
            list_contacts.append(objects[len(objects) - 1])

        history_messenger = None
        chat_name = ''
        last_message_date = ''

        if 'id' in request.GET:
            history_messenger = Chat.objects.filter(id_chat=request.GET['id'])

            try:
                chat_name = history_messenger[len(history_messenger) - 1].name_chat
                last_message_date = history_messenger[len(history_messenger) - 1].date
            except ValueError:
                chat_name = 'Пусто'
                last_message_date = ''

            context = {
                'main': 'on',
                'list_contacts': list_contacts,
                'is_open_settings': open_settings,
                'history_messenger': history_messenger,
                'id_chat': request.GET['id'],
                'chat_name': chat_name,
                'current_email_user': request.user.email,
                'user_name': request.user.username,
                'last_message_date': last_message_date
            }

            return render(request, 'messenger/html/index.html', context)

        context = {
            'main': 'off',
            'list_contacts': list_contacts,
            'is_open_settings': open_settings,
            'user_name': request.user.username,
            'UID': request.user.email[27:31]
        }

        return render(request, 'messenger/html/index.html', context)
    
    elif request.method == 'POST':
        if 'settings' in request.POST:
            if request.POST['settings'] == 'on':
                request.user.username = request.POST['username']
                request.user.save()

                return redirect(reverse('chat'), permanent=True)
    
        elif 'id' in request.POST:
            content_messenger = request.POST['content-messenger']

            if len(content_messenger) == 0:
                return  redirect(reverse('chat') + f'?id={request.POST['id']}', permanent=True)


            name_chat = ''
            history_messenger = Chat.objects.filter(id_chat=request.POST['id'])

            try:
                name_chat = [len(history_messenger) - 1].name_chat
            except ValueError:
                name_chat = 'Пусто'
            except AttributeError:
                name_chat = 'Пусто'

            chat = Chat(
                id_chat = request.POST['id'],
                name_chat = name_chat,
                email_user = request.user.email,
                uid = request.user.email[27:31],
                name_user = request.user.username,
                message = content_messenger,
            )

            chat.save()

            return redirect(reverse('chat') + f'?id={request.POST['id']}', permanent=True)

        else:
            redirect(reverse('chat'), permanent=True)
    else:
        return HttpResponseBadRequest(request)