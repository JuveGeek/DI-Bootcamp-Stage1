from tkinter import CASCADE
from django.db import models

# Create your models here.
class Family(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12)

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE, default='1')

