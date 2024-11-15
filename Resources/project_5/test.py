from django.db import models

class Person(models.Model): # inherit from models.Model
    name=models.CharField(max_length=15)
    age=models.IntegerField()
