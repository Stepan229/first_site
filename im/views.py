
from django.shortcuts import render, redirect
from django.template.defaultfilters import title

data = [
    {"chats": ""},
]
# Create your views here.
def message(request):
    # return redirect('users: login')
    data = {
        'title': 'Сообщения'
    }
    return render(request, 'im/message_menu.html', data)