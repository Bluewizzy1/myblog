from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Post
# Create your views here.


def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'core/frontpage.html', {'posts': posts})


def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User_Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")