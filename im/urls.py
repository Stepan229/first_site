from django.urls import path
from .views import messages, chats

app_name = "mess"
urlpatterns = [
    path('', chats, name="message"),
    path("<int:chat_id>", messages, name="chats"),
]