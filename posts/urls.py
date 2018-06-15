from django.urls import path
from posts.views import get_index, create_or_edit_post, post_detail

urlpatterns = [
    path('new/', create_or_edit_post, name='new_post'),
    path('<pk>/', post_detail, name='post_detail'),
    path('<pk>/edit', create_or_edit_post, name='edit_posts'),
    path('', get_index, name='get_posts')
    ]