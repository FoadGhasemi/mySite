from django.shortcuts import render, redirect
from .models import Project

def projects(request):
    projects_ = Project.objects.all()
    return render(request, "templates/index.html", {"projects_":projects_})

def project_details(request, id):
    project = Project.objects.get(pk = id)
    return render(request, "project_app/project_details.html", {"project": project})

def add_project(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        if title and description:
            Project.objects.create(title = title, description = description, image = image)
            return redirect("home")
    return render(request, "project_app/project_create.html")
