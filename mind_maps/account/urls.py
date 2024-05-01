from django.urls import path
from . import views

urlpatterns = [
    path('sing_in/', views.sing_in, name='sing_in'),
    path('sing_up/', views.sing_up, name='sing_up'),
]