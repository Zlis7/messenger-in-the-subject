from django.shortcuts import render

def index(request):
    return render(request, 'messenger/html/index.html')

def chat(request, id):
    return render(request, 'messenger/html/chat.html')