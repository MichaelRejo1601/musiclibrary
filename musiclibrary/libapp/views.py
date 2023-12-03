from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def home(request):
    return render(request, 'home.html', {})

def artists(request):
    return render(request, 'artists.html', {})

def albums(request):
    return render(request, 'albums.html', {})
