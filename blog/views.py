<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Post
from .forms import PostForm
=======
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
>>>>>>> a405d1494648b5ad3a19afba839c923370898106

# Create your views here.
def post_list(request):
<<<<<<< HEAD
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        [form] = PostForm(request.POST)
    else:
      form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

=======
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
>>>>>>> a405d1494648b5ad3a19afba839c923370898106
