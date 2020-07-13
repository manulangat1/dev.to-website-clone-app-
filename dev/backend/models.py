from django.db import models
from django.contrib.auth.models import AbstractUser
from martor.models import MartorField 
# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.username

class AccountType(models.Model):
    ACCOUNT_TYPES = (
        ('FREE','FREE'),
        ('PRO','PRO'),   
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type  = models.CharField(max_length=25,choices=ACCOUNT_TYPES,default="FREE")
    created = models.DateTimeField(auto_now_add=True)
    valid_through = models.DateTimeField()

    def __str__(self):
        return "{0} type {1}".format(self.user.username,self.type)


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






