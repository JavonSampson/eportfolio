from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hellotimme(requested):
    now=datetime.datetime.now()
    return HttpResponse(f"<Hello,world!</h1> <p> It's {now}.</p>")

def screenprint(request):
    return render(request, "core/screenprint.html")
