
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all_post/', views.post_blog, name="post_blog"),
    path('all_post/make_post/', views.post_content, name="make_post_blog"),
    path('all_post/<slug:slug>/', views.post_id, name="post_id"),
    
]