from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseBadRequest
from .models import Message


@login_required
def index(request):
    if not request.method in ['GET', 'POST']:
        return HttpResponseBadRequest(request)

    else:
        list_contacts = Message.objects.filter(uid=request.user.uid)
        list_contacts_messages = []
        unique_id_chats = []

        for i in list_contacts:
            if i.id_chat not in unique_id_chats:
                unique_id_chats.append(i.id_chat)

        list_contacts = []

        for i in unique_id_chats:
            objects = Message.objects.filter(id_chat=i)
            list_contacts.append(objects[len(objects) - 1])

        for i in list_contacts:
            text = i.content_message
            list_contacts_messages.append(text)

    if request.method == 'GET':
        id = request.GET.get('id')
        history_messenger = []
        chat_name = 'Пусто'
        last_message_date = ''

        if id is not None:
            history_messenger = Message.objects.filter(id_chat=id)

            try:
                chat_name = history_messenger[len(history_messenger) - 1].name_chat
                last_message_date = history_messenger[len(history_messenger) - 1].date
            except ValueError:
                chat_name = 'Пусто'
                last_message_date = ''

        context = {
            'UID': request.user.uid,
            'username': request.user.username,
            'list_contacts':list_contacts,
            'list_contacts_messages':list_contacts_messages,
            'history_messenger': history_messenger,
            'chat_name':chat_name,
            'last_message_date': last_message_date
        }

        return render(request, 'messenger/html/index.html', context)

    elif request.method == 'POST':
        id = request.POST.get('id')
        value_set_username = request.POST.get('value_set_username')
        use_id_chat_for_redirect = ''

        if id is None and value_set_username is None:
            redirect(reverse('index_messenger'), permanent=True)

        else:
            if value_set_username is not None:
                request.user.username = value_set_username
                request.user.save()

            elif id is not None:
                content_message = request.POST['content-message']

                history_messenger = Message.objects.filter(id_chat=id)
                name_chat = ''

                try:
                    name_chat = [len(history_messenger) - 1].name_chat
                except ValueError:
                    name_chat = 'Пусто'
                except AttributeError:
                    name_chat = 'Пусто'

                message = Message(
                    id_chat=id,
                    name_chat=name_chat,
                    uid=request.user.uid,
                    content_message=content_message,
                    date = request.user.last_login
                )

                message.save()
                use_id_chat_for_redirect = f'?id={id}'

            return redirect(reverse('index_messenger') + use_id_chat_for_redirect, permanent=True)