from django.shortcuts import redirect

def index(request):
    return redirect(to='chat/', permanent=True)