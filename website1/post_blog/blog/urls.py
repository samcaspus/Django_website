from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name="index"),
    path('publish', views.publish,name="publish"),
    path('unpublish', views.unpublish,name="unpublish"),
    path('delete', views.delete,name="delete"),
    path('login', views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('entry',views.entry,name="entry"),
]
