from django.db.models.fields.files import ImageField
from django.shortcuts import redirect, render
from.models import info
from django.contrib.auth.models import User,auth

# Create your views here.
def data(req):
    t=info.objects.all()
   
    return render(req,'home.html',{"t":t})
def login(req):
    if req.method=='POST':
       name=req.POST['name']
       password=req.POST['pass']
       

       return redirect('/')
 

    else:
        return render(req,'login.html')
def details(req):
        v=req.GET.get('data')
        print(v)
        
        return render(req,'3.html',{'v':v})
        
    
         