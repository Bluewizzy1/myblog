from django.shortcuts import render
from core.models import Post
# Create your views here.


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'core/frontpage.html', {'post': posts})


def about(request):
    return render(request, 'core/about.html')

