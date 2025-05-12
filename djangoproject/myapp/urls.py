from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name="index"),
    path('hello/<str:username>', views.inge, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="projects_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('about/', views.about, name="about"),
    path('create_tasks/', views.create_tasks, name="create_tasks"),
    path('create_new_project/', views.create_project, name="create_project"),
]