from django.http import HttpResponse
from .models import project,Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTasks, CreateNewProject
# Create your views here.
def hello(request):
    return HttpResponse("<h2> Hola mundo </h2>")

def about(request):
    username = 'Ing Angel'
    return render(request, 'about.html', {'username': username})

def inge(request, username):
    print(username)
    
    return HttpResponse("<h2> hello %s Cada dia mas ingeniero :) </h2>" % username)

def index(request):
    title = 'Bienvenido a mi pagina web'
    return render(request, 'index.html', {'title': title})

def projects(request):
    #projects = list(project.objects.values())
    projects = project.objects.all()
    return render(request, 'project/projects.html', {'projects': projects})

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'tasks/Crear_Tarea.html', {'form': CreateNewTasks()})
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method=='GET':
        return render(request, 'project/Crear_Proyecto.html', {'form': CreateNewProject()})
    else:
        project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    #project.objects.get(id=id)
    projects = get_object_or_404(project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'project/detail.html', {'projects': projects, 'tasks': tasks})