from django.shortcuts import render, redirect, get_object_or_404
from .models import  Post
from .forms import PostForm

# Create your views here.
def post_list(request):
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

