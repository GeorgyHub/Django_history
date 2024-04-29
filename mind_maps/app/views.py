from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, "base.html")

def sing_in(request):
    return render(request, "sing_in.html")

def sing_up(request):
    return render(request, "sing_up.html")