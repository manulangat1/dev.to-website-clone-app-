from django.db import models
from martor.models import MartorField 
# Create your models here.

class BaseModel(models.Model):
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

class Post(BaseModel):
    title = models.CharField(max_length=70)
    body = MartorField()

    def __str__(self):
        return self.title




