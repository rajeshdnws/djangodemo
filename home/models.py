from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class  Contact(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=30);
    email=models.EmailField()
    pwd=models.CharField(max_length=40)
    condition=models.SmallIntegerField()

          
