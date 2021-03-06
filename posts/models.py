from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
  """
  A single Blog post
  """
  title = models.CharField(max_length=200)
  content = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)
  published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
  views = models.IntegerField(default=0)
  tag = models.CharField(max_length=30, blank=True, null=True)
  image = models.ImageField(upload_to="images", blank=True, null=True)
  owner = models.ForeignKey(User, related_name='blogs', null=True, default= 1, on_delete=models.SET_NULL)
  likes = models.ManyToManyField(User, related_name='liked_posts')
  # if you have SET_NULL and for the on_delete and null=True, then the user will show up as "none" if you delete the user. If you have SET_DEFAULT, it will transfer ownership to the admin if the user who posted is deleted. 
  
  def __str__(self):
    return self.title