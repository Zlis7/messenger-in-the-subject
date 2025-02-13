from django.db import models
from datetime import date

class Chat(models.Model):
    id_chat = models.CharField(max_length=68, default = '')
    email_user = models.CharField(max_length=68, default = '')
    message = models.CharField(max_length=5000, default = '')
    date = models.DateField(default = date.today)
