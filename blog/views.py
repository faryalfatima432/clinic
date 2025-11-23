from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from .models import Blog

def blogs(request):
    blogs=get_list_or_404(Blog)
    return HttpResponse(blogs)

def blogDetails(request,id):
    blog=get_object_or_404(Blog,id=id)
    print(blog.title,blog.content)
    print(blog)
    return HttpResponse(blog)
