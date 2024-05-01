from django.shortcuts import render
from django.template import loader
from .models import Person, Questions

# Create your views here.
def home(request):
    person = Person.objects.all()
    quest = Questions.objects.all()
    context = {
        'person': person,
        'quest': quest,
        'title': 'Главная'
    }
    return render(request, "base.html", context=context)

