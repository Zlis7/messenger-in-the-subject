from django.db import models
from datetime import date

class Chats(models.Model):
    id_chat = models.IntegerField(max_length=100000, default = 0)
    id_user = models.IntegerField(max_length=100000, default = 0)
    message = models.CharField(max_length=5000, default = '')
    date = models.DateField(default = date.today)