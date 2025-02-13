from django.urls import path
from messenger import views

urlpatterns = [
    path('', views.index, name='home-chat'),
    path('<slug:id>', views.chat, name='chat')
]
