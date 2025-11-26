from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Comment


def blogs(request):
    blogs = get_list_or_404(Blog)
    return render(request, "blogs.html", {'blogs':blogs})


def blogDetails(request, id):
    blog = get_object_or_404(Blog, id=id)
    comments = Comment.objects.filter(blog=id)
    return render(request, "blog.html", {'blog': blog, 'comments': comments})
