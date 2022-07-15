from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.description} {self.date}"
