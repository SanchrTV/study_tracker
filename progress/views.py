from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'progress/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'progress/add_task.html', {'form': form})
