from django.db import models
from django.forms import ModelForm, TextInput

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 2500)
    importance = models.CharField(max_length = 50, default='medium')


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
        'title': TextInput(attrs={"type": "text"}),
        'description': TextInput(attrs={"type": "text"}),
        'importance': TextInput(attrs={"type": "text"})
        }
    # def clean_date(self):
    #     d = self.cleaned_data.get("date")
    #     if d < date.today():
    #         raise ValidationError("Meetings cannot be in the past")
    #     return d
