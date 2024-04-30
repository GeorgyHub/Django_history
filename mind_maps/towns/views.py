from django.shortcuts import render
from .models import Place

# Create your views here.
def town(request):
    town = Place.objects.all()
    return render(request, 'index.html')