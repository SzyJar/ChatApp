from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chatroom/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'chatroom/room.html', {'rooms': room, 'messages': messages})

@login_required
def clear_room(request, slug):
    room = Room.objects.get(slug=slug)
    room.messages.all().delete()

    rooms = Room.objects.all()
    return render(request, 'chatroom/rooms.html', {'rooms': rooms})
