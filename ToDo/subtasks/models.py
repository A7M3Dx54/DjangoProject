from django.db import models
from tasks import models as tm
from django.contrib.auth.models import User
from django.forms import ChoiceField, ModelForm, TextInput

# Create your models here.

class Subtask(models.Model):
    task = models.ForeignKey(tm.Task, on_delete=models.CASCADE)
    users = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 2500)
    importance = models.CharField(max_length = 50)

class SubtaskForm(ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'description', 'importance', 'users']
        widgets = {
        'title': TextInput(attrs={"type": "text"}),
        'description': TextInput(attrs={"type": "text"}),
        'importance': TextInput(attrs={"type": "text"})
        }