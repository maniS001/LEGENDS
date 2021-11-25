from django.shortcuts import render,redirect
from django.db.models.fields.files import ImageField
from django.db import models
from django.db.models.fields import IntegerField
from LEADERS.models import info
def albert(req):
    
    return render(req,'albert.html')
def elon(req):
    return render(req,'elon.html')
def abdul(req):
    return render(req,'abdul.html')
def tesla(req):
    return render(req,'tesla.html')
    


    
   
