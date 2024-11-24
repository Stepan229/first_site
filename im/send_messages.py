from django.template.defaultfilters import title
from django.utils.dateparse import parse_date
from .models import UserMessages, Chat, Message


def save_mess_db(text, id_userMessages, user_id):
    message = Message(text=text,
                      UserMessages_id=UserMessages.objects.get(id=id_userMessages),
                      creator_id=user_id)
    message.save()
    pass

def find_chats_user(user_id):
    id_userMessages_chat = UserMessages.objects.filter(user_id=1).values('chat_id', 'id')
    id_chats = []
    id_userMessages = []
    for id in id_userMessages_chat:
        id_chats.append(id['chat_id'])
        id_userMessages.append(id['id'])
    title_chats = Chat.objects.filter(id__in=id_chats).values_list('title', flat=True)
    chats = dict(zip(id_userMessages, title_chats))
    return chats

def find_messages_chat(id_userMessage):
    # columns = ['creator_id', 'text', 'time_create', 'is_read']
    query_messages = Message.objects.filter(UserMessages_id=id_userMessage).order_by('time_create')
    query_messages = query_messages.values('creator_id', 'text', 'time_create', 'is_read')
    messages = list(query_messages)
    return messages



