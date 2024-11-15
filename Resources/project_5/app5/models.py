from django.db import models

# Create your models here.

class student(models.Model):
      name=models.CharField(max_length=20)
      roll=models.IntegerField(primary_key=True)
      address=models.TextField()
      age=models.IntegerField(default=0)
      def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Age: {self.age}, Address: {self.address}"