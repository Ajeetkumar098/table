from django.db import models

# Create your models here.

class student (models.Model):
    name=models.CharField( max_length=100)
    age=models.PositiveBigIntegerField()
    email=models.EmailField()
    rollno=models.IntegerField()
    mobileno=models.IntegerField()
    address=models.CharField(max_length=20)