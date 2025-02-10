from django.db import models

class Tokens(models.Model):
    value = models.CharField(max_length=7)
