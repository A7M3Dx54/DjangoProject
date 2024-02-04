from django.shortcuts import render
from tasks.models import Task

# Create your views here.
def home_view(request):
    context ={'tasks': Task.objects.all()}
    return render(request, "website/home.html", context=context)
 