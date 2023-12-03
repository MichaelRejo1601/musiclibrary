from django.contrib import admin
from libapp.models import *

# Register your models here.

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(Csv)
admin.site.register(Playlist)
admin.site.register(Playsong)
admin.site.register(Song)
admin.site.register(Users)