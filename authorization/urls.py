from django.urls import path
from authorization import views

urlpatterns = [
    path('login', views.login, name='home'),
    path('regis', views.authorization, name='chat'),
    path('register_confirm/<token>/', views.register_confirm, name='register_confirm')    
]
