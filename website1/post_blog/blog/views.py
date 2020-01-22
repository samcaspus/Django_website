from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import blogging

# Create your views here.
def index(request):
    data = blogging.objects.all().order_by("-id")
    return render(request,'index.html',{'messages':data})

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username = username,password=password)
    if user is not None:
        auth.login(request,user)
    return redirect('/loggedin')

def publish(request):
    identity = request.POST["identity"]
    blogging.objects.filter(id=identity).update(publish=True)
    return redirect('/')

def unpublish(request):
    identity = request.POST["identity"]
    blogging.objects.filter(id=identity).update(publish=False)
    return redirect('/')
    
def entry(request):
    username = request.POST["username"]
    blog = request.POST["blog"]
    # print(username,blog)
    b = blogging(user = username, data = blog)
    b.save(force_insert=True)
    return redirect('/entered')

def delete(request):
    identity = request.POST["identity"]
    blogging.objects.get(id=identity).delete()
    return redirect('/deleted')


def logout(request):
    auth.logout(request)
    return redirect('/loggedout')

def loggedin(request):
    return redirect('/')

def loggedout(request):
    return redirect('/')

def deleted(request):
    return redirect('/')

def entered(request):
    return redirect('/')

    
