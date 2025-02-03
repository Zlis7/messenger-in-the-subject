from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('chat/', include('messenger.urls'), name='messenger')
]
