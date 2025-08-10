from django.shortcuts import render , redirect
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
    return redirect('index')
9
def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('index')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('index')