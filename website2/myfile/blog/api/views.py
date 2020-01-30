from django.shortcuts import render

from blog.models import Article
from blog.api.serializers import BlogSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
@api_view(['GET',])
def post_blog(request):
    try:
        blog_post = Article.objects.all()
    except:
        data = {}
        data["invalid"] = "response is invalid"
        return Response(data)

    serialized = BlogSerializer(blog_post, many=True)
    return Response(serialized.data)


@csrf_exempt
@api_view(['GET',])
def post_id(request,slug):
    try:
        blog_post = Article.objects.get(id=slug)
    except:
        data = {}
        data["invalid"] = "response is invalid"
        return Response(data)

    serialized = BlogSerializer(blog_post)
    return Response(serialized.data)




@api_view(['POST',])
def post_content(request):
    try:
        blog_post = Article()
    except:
        data = {}
        data["invalid"] = "response is invalid"
        return Response(data)
    serialized = BlogSerializer(blog_post,data = request.data)
    if serialized.is_valid():
        serialized.save()
        return Response({"sucess":"data is posted"})
    else:
        return Response(serialized.error)


