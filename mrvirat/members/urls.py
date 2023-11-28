from django.urls import path
from .views import chat, send_message

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('virat/', lambda request: send_message(request, 'msVirat'), name='send_virat'),
    path('anushka/', lambda request: send_message(request, 'mrsAnushka'), name='send_anushka'),
]
