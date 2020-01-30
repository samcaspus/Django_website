from django.shortcuts import render

from blog.models import Article
# Create your views here.

def index(request):
    data = Article.objects.all().order_by("-id")
    return render(request,"index.html",{"message" : data})