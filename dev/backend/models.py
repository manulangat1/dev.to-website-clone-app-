from django.db import models
from django.contrib.auth.models import AbstractUser
from martor.models import MartorField 
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.bio




class BaseModel(models.Model):
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

class Post(BaseModel):
    title = models.CharField(max_length=70)
    body = MartorField()

    def __str__(self):
        return self.title

    def get_likes_all(self):
        return self.likes.count()
    def get_dislikes_all(self):
        return self.dislikes.count()

class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.post.title

class Dislikes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="dislikes")
    dislikes = models.PositiveIntegerField()

    def __str__(self):
        return self.post.title






