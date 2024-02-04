from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from accounts.models import UserForm
from website import views as wv

# Create your views here.

def all_users(request):
    users = User.objects.all()
    return render(request, "accounts.html", {'users':users})

def add(request):
    form=UserForm()
    return render(request, "add.html",{"form": form})


@require_POST
def add_user(request):
    form = UserForm(data=request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return detail(request, user.id)
    
def detail(request, id):
    user = User.objects.get(pk=id)
    return render(request, "detail.html", {"user": user})


def edit(request,id):
    user = User.objects.get(pk=id)
    form=UserForm(instance=user)
    return render(request, "edit.html",{"form": form,
                                              "user":user
                                              })


def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return all_users(request)

@require_POST
def edit_user(request,id):
    user = User.objects.get(pk=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return detail(request,id)