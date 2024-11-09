from django.template.defaultfilters import title

from .models import UserMessages, Chat
from django.db import models

def save_mess_db(text):
    pass

def find_chats_user(user_id):
    # print(user_id, " user")
    id_chats = UserMessages.objects.filter(user_id=user_id)
    chats_title = []
    for chat in id_chats:
        chats_title.append(str(chat.chat_id))
    return chats_title