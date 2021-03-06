from django.db import models
from django.contrib.auth.models import AbstractUser
from martor.models import MartorField 
# Create your models here.
class BaseModel(models.Model):
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

class User(AbstractUser):
    bio = models.TextField(blank=True,null=True)
    friends = models.ManyToManyField('User',blank=True,null=True)
    def __str__(self):
        return self.username

class AccountType(models.Model):
    ACCOUNT_TYPES = (
        ('FREE','FREE'),
        ('PRO','PRO'),   
    )
    
    type  = models.CharField(max_length=25,choices=ACCOUNT_TYPES,default="FREE")
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    valid_through = models.DateTimeField()

    def __str__(self):
        return "{0} costs {1}".format(self.type, self.price)

class UserMembership(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    membership = models.ForeignKey(AccountType,on_delete=models.CASCADE)

    def __str__(self):
        return "{0} type {1}".format(self.user.username,self.membership.type)

# class SubScriptio
class Post(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
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
    likes = models.BooleanField(default=False)
    user = models.ForeignKey(User,related_name="likes",on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.post.title

class Dislikes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="dislikes")
    dislikes = models.PositiveIntegerField()

    def __str__(self):
        return self.post.title


class FriendRequest(BaseModel):
    to_user = models.ForeignKey(User,related_name="to_user",on_delete=models.CASCADE)
    from_user = models.ForeignKey(User,related_name="from_user",on_delete=models.CASCADE)

    def __str__(self):
        return " From {0} to {1}".format(self.from_user.username,self.to_user.username)


