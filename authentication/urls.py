from authentication import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_auth'),
    path('confirmation_registration/<slug:token>/', views.confirmation_registration, name='confirmation_registration'),
    path('logout/', views.logout, name='logout')
]
