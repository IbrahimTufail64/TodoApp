from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TaskForm

# Create your views here.


def index(request):
    task = tasks.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'task': task, 'form': form}
    return render(request, 'task/index.html', context)


def update(request, pk):
    task = tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'task/update.html', {'form': form})


def delete(request, pk):
    task = tasks.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'task/delete.html', {'task': task, 'form': form})
