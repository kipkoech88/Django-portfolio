from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=128) 
    def __str__(self):
        return self.name 

class Service(models.Model):
    category=models.CharField(max_length=128) 
    specifications=models.CharField(max_length=128) 
    price=models.IntegerField() 
    def __str__(self):
        return self.category