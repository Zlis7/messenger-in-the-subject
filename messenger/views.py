from django.shortcuts import render
from .models import Chats

def index(request):
    context = {
        'main': 'off'
    }

    return render(request, 'messenger/html/index.html', context)

def chat(request, id):
    list_contacts = Chats.objects.filter(id_user = request.user.id).order_by("-date")

    context = {
        'main': 'on',
        'list_contacts': list_contacts,
        'id_chat': id,
        'id_user': request.user.id
    }

    return render(request, 'messenger/html/index.html', context)