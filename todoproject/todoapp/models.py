from django.db import models

# Create your models here.

class Task(models.Model):
    label = models.CharField(max_length=250)
    priority = models.IntegerField()
    tdate = models.DateField()

    def __str__(self):
        return self.label
