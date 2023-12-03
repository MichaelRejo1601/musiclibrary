from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['u_username', 'u_password']