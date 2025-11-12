from django.shortcuts import render, redirect
from . models import Ticket

def ticket_create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        email = request.POST.get("email")
        gist = request.POST.get("gist")
        body = request.POST.get("body")
        if title and body:
            Ticket.objects.create(title=title, body=body, email=email, gist=gist)
            return redirect("home")
    return render(request, "index.html")



