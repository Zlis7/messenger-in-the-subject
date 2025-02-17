from django.urls import path
from messenger import views

urlpatterns = [
    path('', views.index, name='index_messenger')
]
