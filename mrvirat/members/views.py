
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Message

def chat(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages,'current_time': timezone.now()})

def send_message(request, sender):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(sender=sender, content=content, timestamp=timezone.now())
    return redirect('chat')
