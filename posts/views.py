from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from textblob import TextBlob

# Create your views here - POSTS.
def get_index(request): 
    if request.user.is_authenticated:
        blogs = Post.objects.all()
    else: 
        blogs = Post.objects.all()
    return render(request, 'posts/index.html', {'blogs': blogs})

def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if not post.owner:
                post.owner = request.user
            post.save()
            return redirect('/')
            # return redirect(post_detail, post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/blogpostform.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})