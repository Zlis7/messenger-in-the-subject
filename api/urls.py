from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('chat/', include('messenger.urls'), name='messenger'),
    path('auth/', include('authentication.urls'), name='authentication')
]
