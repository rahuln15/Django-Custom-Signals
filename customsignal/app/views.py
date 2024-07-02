from django.shortcuts import render, HttpResponse
from app import signals
# Create your views here.

def home(request):
    signals.notification.send(sender=None, request=request, user=['om','uikey'])
    return HttpResponse("Home Page")
