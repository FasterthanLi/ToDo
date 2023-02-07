from django.conf import settings
from django.db import models

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} by {self.author} - {self.deadline}"