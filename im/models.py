from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Chat(models.Model):
    title = models.CharField(max_length=70)
    time_create = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class UserMessages(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_read = models.BooleanField(default=False) # показывает что у тебя не прочитано сообщение


class Message(models.Model):
    creator_id = models.IntegerField()
    UserMessages_id = models.ForeignKey(UserMessages, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    time_create = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False) # прочитал ли кто-то твое сообщение

    def __str__(self):
        return self.text

