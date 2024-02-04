from django.shortcuts import render
from subtasks.models import Subtask
from subtasks.models import SubtaskForm
from tasks.models import Task
from website import views as wv
from django.views.decorators.http import require_POST
# Create your views here.

def sub_detail(request, id):
    subtask = Subtask.objects.get(pk=id)
    return render(request, "subtasks/sub_detail.html", 
                  {"subtask": subtask,}
                )

@require_POST
def add(request, id):
    print("hereee")
    form = SubtaskForm(data=request.POST)
    task = Task.objects.get(pk=id)
    if form.is_valid():
        subtask = form.save(commit=False)
        subtask.task = task
        subtask.save()
        return sub_detail(request,subtask.id)
    
def edit(request,id):
    subtask = Subtask.objects.get(pk=id)
    form=SubtaskForm(instance=subtask)
    return render(request, "subtasks/edit.html",{"form": form,
                                        "subtask":subtask})

def delete_subtask(request, id):
    subtask = Subtask.objects.get(pk=id)
    subtask.delete()
    return wv.home_view(request)

@require_POST
def edit_subtask(request,id):
    subtask = Subtask.objects.get(pk=id)
    form = SubtaskForm(request.POST,instance=subtask)
    if form.is_valid():
        form.save()
        return sub_detail(request,id)