from django.db import models

# Create your models here.

class Course (models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    hour=models.CharField(max_length=15)
    credits=models.CharField(max_length=30)
    state=models.CharField(max_length=15)

class Career (models.Model):
    name=models.CharField(max_length=50)
    shortname=models.CharField(max_length=30)
    description=models.TextField()
    imagen=models.TextField()
    state=models.CharField(max_length=15)
