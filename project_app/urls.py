from django.urls import path
from . import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("create", views.add_project, name="project_create"),
    path("details/<int:id>", views.project_details, name="project_details"),
]
