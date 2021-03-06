from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from textblob import TextBlob
from django.http import HttpResponseForbidden

# Create your views here - POSTS.
def get_index(request): 
    if request.user.is_authenticated:
        blogs = Post.objects.all()
    else: 
        blogs = Post.objects.all()
    return render(request, 'posts/index.html', {'blogs': blogs})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        
    return render(request, 'posts/blogpostform.html', {'form': form})
        
        
def edit_post(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated and request.user == post.owner or request.user.is_superuser: 
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect('post_detail', post.pk)        
        else:
            form = PostForm(instance=post)
    else: 
        return HttpResponseForbidden()
        
    return render(request, 'posts/blogpostform.html', {'form': form})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})