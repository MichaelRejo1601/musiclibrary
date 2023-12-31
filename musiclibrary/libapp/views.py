from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .forms import *

from .models import *

# Create your views here.

def base(request):
    return render(request, 'base.html', {})

@login_required
@csrf_exempt
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name is not None:
            newobj = Playlist(p_name=name, p_uid = Users.objects.get(u_username=request.user.username))
            newobj.save()
    playlists = Playlist.objects.select_related('p_uid').all().filter(p_uid__u_username = request.user.username)
    return render(request, 'home.html', {"playlists" : playlists})

@login_required
@csrf_exempt
def test(request):
    songs = Song.objects.select_related('s_alid__al_aid').all()
    
    return render(request, 'index.html', {'songs': songs})

@login_required
@csrf_exempt
def search_artists(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        artists = Artist.objects.filter(a_name__icontains=search_query)
    else:
        artists = []

    return render(request, 'artists.html', {'artists': artists})

@login_required
@csrf_exempt
def artist_albums(request, artist_id):
    artist = get_object_or_404(Artist, a_aid=artist_id)
    albums = Album.objects.filter(al_aid=artist)
    return render(request, 'artist_albums.html', {'artist': artist, 'albums': albums})

@login_required
@csrf_exempt
def search_albums(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        condition_A = Q(al_name__icontains=search_query)
        condition_B = Q(al_aid__a_name__icontains=search_query)
        combined_condition = condition_A  | condition_B
        albums = Album.objects.select_related('al_aid').all().filter(combined_condition)
    else:
        albums = []

    return render(request, 'albums.html', {'albums': albums})

@login_required
@csrf_exempt
def album_songs(request, album_id):
    album = Album.objects.select_related('al_aid').all().get(al_alid = album_id)
    songs = Song.objects.filter(s_alid=album)
    return render(request, 'album_songs.html', {'album': album, 'songs': songs})
   
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            new_user = Users(u_username=username, u_password=password)
            new_user.save()
            
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('/login') 
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
@csrf_exempt
def remove(request, playlist_id):
    obj = Playlist.objects.get(p_pid = playlist_id)
    if obj:
        obj.delete()
    return redirect("/home")

@login_required
@csrf_exempt
def playlist(request, playlist_id):
    danceability_status = False
    playlist = get_object_or_404(Playlist, p_pid=playlist_id)
    playlist_instance = Playlist.objects.get(p_pid=playlist_id)
    playsongs = Playsong.objects.select_related('ps_sid__s_alid__al_aid').filter(ps_pid=playlist_instance)
    
    if 'search' in request.GET:
        search_query = request.GET['search']
        # Use contains so as long as search contains some correct letters we are good
        condition_A = Q(s_name__icontains=search_query)
        condition_B = Q(s_alid__al_aid__a_name__icontains=search_query)
        condition_C = Q(s_alid__al_name__icontains=search_query)
        combined_condition = condition_A  | condition_B | condition_C
        song_ids_in_playlist = [playsong.ps_sid.s_sid for playsong in playsongs]
        songs = Song.objects.select_related('s_alid__al_aid').all().filter(combined_condition).exclude(s_sid__in=song_ids_in_playlist)
        
    else:
        search_query=" "
        songs = []
        
    if 'danceabilityStatus' in request.GET:
        danceabilityStatus = request.GET['danceabilityStatus']
        danceability_status = danceabilityStatus.lower() == 'true'
    
    print(danceability_status)
    if danceability_status:
        playsongs = playsongs.filter(ps_sid__s_danceability__gt=0.5)
        print("filtered")
        
    return render(request, 'playlist.html', {'playlist': playlist, 'playsongs':playsongs, 'songs':songs, 'search_query':search_query, 'danceability_status':danceability_status})

@login_required
@csrf_exempt
def add_song(request, playlist_id, song_id, search_query):
    obj = Playsong(playlist_id, song_id)
    obj.save()
    return redirect("/playlist/{0}/?search={1}".format(playlist_id, search_query))

@login_required
@csrf_exempt
def remove_song(request, playlist_id, song_id, search_query):
    obj = Playsong.objects.filter(ps_pid=playlist_id, ps_sid=song_id).first()
    if obj:
        obj.delete()
    return redirect("/playlist/{0}/?search={1}".format(playlist_id, search_query))