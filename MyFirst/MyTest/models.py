from django.db import models

# Create your models here.
class Person2(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()