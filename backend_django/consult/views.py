# consult/views.py
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "consult/index.html")

def room(request, room_name):
    return render(request, "consult/room.html", {"room_name": room_name})
