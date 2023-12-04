"""musiclibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Page navigation
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('search_artists/', views.search_artists, name='search_artists'),
    path('search_albums/', views.search_albums, name='search_albums'),
   
    # Search artists
    path('artist_albums/<int:artist_id>/', views.artist_albums, name='artist_albums'),

    # Search albums
    path('album_songs/<int:album_id>/', views.album_songs, name='album_songs'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('remove/<int:playlist_id>/', views.remove, name="remove"),

    # See playlist
    path('playlist/<int:playlist_id>/', views.playlist, name='playlist'),
    path('playlist/<int:playlist_id>/add_song/<int:song_id>/query/<str:search_query>/', views.add_song, name="add_song")
]
