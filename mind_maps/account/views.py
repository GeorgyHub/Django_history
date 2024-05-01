from django.shortcuts import render

# Create your views here.
def sing_in(request):
    return render(request, "sing_in.html")

def sing_up(request):
    return render(request, "sing_up.html")