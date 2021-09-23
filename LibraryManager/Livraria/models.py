from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    Title = models.CharField(max_length=80)
    Presser = models.CharField(max_length=50)
    Author = models.CharField(max_length=80)
    Pages = models.IntegerField()
    Description = models.TextField()
    Price = models.FloatField()
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)