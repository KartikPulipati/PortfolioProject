from django.db import models

class Blogs(models.Model):
    title = models.CharField(max_length=100)

    description = models.CharField(max_length=25)

    text = models.TextField()

    TimeModified = models.DateField(auto_now=True, auto_now_add=False)
    TimeCreated = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title





