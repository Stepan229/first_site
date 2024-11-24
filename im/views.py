
from django.shortcuts import render, redirect
from django.template.defaultfilters import title, first
from .forms import SendMessForm
from .send_messages import save_mess_db, find_chats_user, find_messages_chat

data = {
    "chats": ["Матвей", "Лев", "Семен", "Максим"],
    "title": "Сообщения",
    "user": {"first_name": "Степан", "last_name": "Скрылёв", "id": 1},
    "messages": [{"text": "Привет", "user_id": 1, "date": "01.02.03"}, {"text": "Как дела?", "user_id": 2, "date": "01.02.05"}],
}


# Create your views here.
def chats(request):
    # data["form"] = SendMessForm()
    data["chats"] = find_chats_user(request.user.id)
    return render(request, 'im/message_menu.html', data)

def messages(request, chat_id):
    data["messages"] = find_messages_chat(chat_id)
    if request.method == 'POST':
        form = SendMessForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            save_mess_db(cd["text"], chat_id, request.user.id)
            data["messages"].append({"text": cd["text"], "creator_id": request.user.id, "date": None})
            return render(request, 'im/messages.html', data)
    else:

        form = SendMessForm()
    data['form'] = form
    return render(request, 'im/messages.html', data)
