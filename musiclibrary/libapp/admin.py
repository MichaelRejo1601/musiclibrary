from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Album)
admin.site.register(models.Artist)
admin.site.register(models.AuthGroup)
admin.site.register(models.AuthGroupPermissions)
admin.site.register(models.AuthPermission)
admin.site.register(models.AuthUser)
admin.site.register(models.AuthUserGroups)
admin.site.register(models.AuthUserUserPermissions)
admin.site.register(models.Csv)
admin.site.register(models.Playlist)
admin.site.register(models.Playsong)
admin.site.register(models.Song)
admin.site.register(models.Users)