from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('register_confirm/<slug:token>/', views.register_confirm, name='register_confirm'),
    path('logout/', views.logout, name='logout')
]
