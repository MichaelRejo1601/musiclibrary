from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
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

def search_artists(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        # Use contains so as long as search contains some correct letters we are good
        artists = Artist.objects.filter(a_name__icontains=search_query)
    else:
        artists = []

    return render(request, 'artists.html', {'artists': artists})

def artist_albums(request, artist_id):
    artist = get_object_or_404(Artist, a_aid=artist_id)
    albums = Album.objects.filter(al_aid=artist)
    return render(request, 'artist_albums.html', {'artist': artist, 'albums': albums})

def search_albums(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        # Use contains so as long as search contains some correct letters we are good
        albums = Album.objects.filter(al_name__icontains=search_query)
    else:
        albums = []

    return render(request, 'albums.html', {'albums': albums})

def album_songs(request, album_id):
    album = get_object_or_404(Album, al_alid=album_id)
    songs = Song.objects.filter(s_alid=album)
    return render(request, 'album_songs.html', {'album': album, 'songs': songs})
    