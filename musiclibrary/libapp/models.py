# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    al_alid = models.IntegerField(primary_key=True)
    al_name = models.CharField(max_length=64, blank=True, null=True)
    al_aid = models.ForeignKey('Artist', models.DO_NOTHING, db_column='al_aid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class Artist(models.Model):
    a_aid = models.IntegerField(primary_key=True)
    a_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Csv(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    album_id = models.IntegerField(blank=True, null=True)
    album = models.CharField(max_length=64, blank=True, null=True)
    artist_id = models.IntegerField(blank=True, null=True)
    artists = models.CharField(max_length=32, blank=True, null=True)
    track_number = models.IntegerField(blank=True, null=True)
    explicit = models.BooleanField(blank=True, null=True)
    danceability = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csv'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Playlist(models.Model):
    p_pid = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=64, blank=True, null=True)
    p_uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='p_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlist'


class Playsong(models.Model):
    ps_pid = models.OneToOneField(Playlist, models.DO_NOTHING, db_column='ps_pid', primary_key=True)
    ps_sid = models.ForeignKey('Song', models.DO_NOTHING, db_column='ps_sid')

    class Meta:
        managed = False
        db_table = 'playsong'
        unique_together = (('ps_pid', 'ps_sid'),)


class Song(models.Model):
    s_sid = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=64, blank=True, null=True)
    s_tracknum = models.IntegerField(blank=True, null=True)
    s_explicit = models.BooleanField(blank=True, null=True)
    s_danceability = models.FloatField(blank=True, null=True)
    s_alid = models.ForeignKey(Album, models.DO_NOTHING, db_column='s_alid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song'


class Users(models.Model):
    u_uid = models.AutoField(primary_key=True)
    u_username = models.CharField(max_length=64, blank=True, null=True)
    u_password = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
