from django.db import models

class Ticket (models.Model):
    title = models.CharField(max_length= 50)
    email = models.EmailField(default= "blog!")
    gist = models.TextField(default= "blog!")
    body = models.TextField(default= "blog!")

    def __str__(self):
        return f"{self.title} - {self.gist[:10]}"

class Contact_us (models.Model):
    post = models.CharField(max_length= 50)
    neighborhood = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 50)
    email = models.EmailField()

    whatsapp = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
