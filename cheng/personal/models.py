from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    des = models.TextField()
    pub = models.DateTimeField()
    update = models.DateTimeField()
    img_url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
