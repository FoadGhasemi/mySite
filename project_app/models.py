from django.db import models

class Project (models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField(default= "blog!")
    image = models.ImageField( upload_to= "project_app/img/",
                               default="project_app/img/13.PNG")
    def __str__(self):
        return f"{self.title} - {self.description[:10]}"