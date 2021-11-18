from django.db import models
from django.db.models.fields import IntegerField



class info(models.Model):
   name=models.CharField(max_length=50)
   nickname=models.CharField(max_length=30)
   period=models.CharField(max_length=10)
   nationality=models.CharField(max_length=20)
   image=models.ImageField(upload_to='pics')
   rank=IntegerField()
    
# Create your models here.
