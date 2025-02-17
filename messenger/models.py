from django.db import models

class Message(models.Model):
    id_chat = models.CharField(default='', max_length=10, blank=False, null=False)
    name_chat = models.CharField(default='', max_length=20, blank=False, null=False)
    uid = models.CharField(default='', max_length=6, blank=False, null=False)
    content_message = models.CharField(default='', max_length=500, blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.id_chat

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"