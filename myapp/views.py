from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    if request.method=='POST':
        try:
            userobj= User.objects.get(email=request.POST['email'])
            if request.POST['password']==userobj.password:
                return redirect('index')
            else:
                return render(request,'login.html',{'msg':'Invalid password'})
        except:
            return render(request,'login.html',{'msg':'email not found'})
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['cnfpassword']:
            User.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            return redirect('login')
        else:
            return render(request,'register.html',{'msg':'passwords do not match'})
    return render(request,'register.html')