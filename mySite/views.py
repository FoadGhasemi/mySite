from django.shortcuts import render, redirect
from project_app.models import Project
from ticket_app.models import Ticket, Contact_us


def home(request):
    contact_us = Contact_us.objects.all().last()
    projects_ = Project.objects.all()
    if request.method == 'POST':
        title = request.POST.get("title")
        email = request.POST.get("email")
        gist = request.POST.get("gist")
        body = request.POST.get("body")
        if title and body:
            Ticket.objects.create(title=title, body=body, email=email, gist=gist)
            return redirect("home")
    return render(request, "index.html", {"projects_": projects_,
                                          "contact_us": contact_us})
