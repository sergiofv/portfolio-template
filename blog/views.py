from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def blogs(request):
    blogs = Blog.objects  # select all the objects from the class Blog
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
