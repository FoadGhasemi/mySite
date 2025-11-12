from django.urls import path
from . import views

urlpatterns = [
    #path("", views.projects, name="projects"),
    path("create", views.ticket_create, name="ticket_create"),
]
