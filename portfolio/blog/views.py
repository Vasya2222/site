from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.

def blog(request):
    blog = Blog.objects.all()

    return render(request, 'blog/blog.html', {'blogs': blog})


def detail(request, id_blog):
    blog = get_object_or_404(Blog, pk=id_blog)
    return render(request, 'blog/detail_blog.html', {'detail_blog': blog})
