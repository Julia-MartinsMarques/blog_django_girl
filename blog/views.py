<<<<<<< HEAD
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

=======
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post})
    
>>>>>>> 71270476b6efdebb393336d8edc32f2486ac2bf4
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
<<<<<<< HEAD
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
=======
        [form] = PostForm(request.POST)
>>>>>>> 71270476b6efdebb393336d8edc32f2486ac2bf4
    else:
      form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

<<<<<<< HEAD
    
=======
>>>>>>> 71270476b6efdebb393336d8edc32f2486ac2bf4
