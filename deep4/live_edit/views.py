# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "live_edit/base.html")


def room(request, room_name):
    return render(request, "live_edit/base.html", {"room_name": room_name})


# Create your views here.
