from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from .models import Post

# Create your views here.
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    form = CommentForm()
    return render(request, 'blogs/detail.html', {'post':post, 'form':form})