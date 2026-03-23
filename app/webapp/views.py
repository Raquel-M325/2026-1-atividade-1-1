from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá Professor! Sou sua aluna Raquel em SO!")

# Create your views here.
