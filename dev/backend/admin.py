from django.contrib import admin
from django.db import  models
from martor.widgets import AdminMartorWidget
from .models import Post

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':AdminMartorWidget}
    }

admin.site.register(Post,PostModelAdmin)