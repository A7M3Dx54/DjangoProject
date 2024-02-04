from django.shortcuts import render
from .models import Task, TaskForm
from django.views.decorators.http import require_POST
from website import views as wv
from subtasks.models import Subtask
from subtasks.models import SubtaskForm
def detail(request, id):
    task = Task.objects.get(pk=id)
    subTasks=Subtask.objects.filter(task=task.id).all()
    subtaskForm = SubtaskForm()
    return render(request, "tasks/detail.html", {"task": task,
                                                 "subtasks":subTasks,
                                                 "subtaskForm": subtaskForm
                                                 })

def add(request):
    form=TaskForm()
    return render(request, "tasks/add.html",{"form": form})

def edit(request,id):
    task = Task.objects.get(pk=id)
    form=TaskForm(instance=task)
    return render(request, "tasks/edit.html",{"form": form,
                                              "task":task
                                              })

@require_POST
def add_task(request):
    form = TaskForm(data=request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.save()
        return detail(request,task.id)

def delete_task(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return wv.home_view(request)

@require_POST
def edit_task(request,id):
    task = Task.objects.get(pk=id)
    form = TaskForm(request.POST,instance=task)
    if form.is_valid():
        form.save()
        return detail(request,id)