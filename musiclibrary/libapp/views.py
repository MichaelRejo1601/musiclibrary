from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def test(request):
    songs = Song.objects.select_related('s_alid__al_aid').all()
    
    return render(request, 'index.html', {'songs': songs})