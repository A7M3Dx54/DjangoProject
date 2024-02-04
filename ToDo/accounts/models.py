from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

# Create your models here.

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
        'username': TextInput(attrs={"type": "text"}),
        'password': TextInput(attrs={"type": "password"})
        }