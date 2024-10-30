from django.urls import path
from .views import message

app_name = "mess"
urlpatterns = [
    path('', message, name="message"),
]