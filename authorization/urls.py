from django.urls import path
from authorization import views

urlpatterns = [
    path('', views.login, name='home'),
    path('<slug:id>', views.authorization, name='chat')
]
