from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    return render(request, 'messenger/html/index.html')

@login_required
def chat(request, id):
    return render(request, 'messenger/html/chat.html')