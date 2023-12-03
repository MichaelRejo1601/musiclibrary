from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def home(request):
    return render(request, 'home.html', {})

def artists(request):
    return render(request, 'artists.html', {})

def albums(request):
    return render(request, 'albums.html', {})

def test(request):
    songs = Song.objects.select_related('s_alid__al_aid').all()
    
    return render(request, 'index.html', {'songs': songs})
