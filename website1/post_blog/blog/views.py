from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import blogging

# Create your views here.
def index(request):
    data = blogging.objects.all()
    return render(request,'index.html',{'messages':data})

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username = username,password=password)
    if user is not None:
        auth.login(request,user)
    
    return redirect('/')
    



def entry(request):
    username = request.POST["username"]
    blog = request.POST["blog"]
    print("dsfsdsadsdsacs",username,blog)
    b = blogging(user = username, data = blog)
    b.save(force_insert=True)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')
    
