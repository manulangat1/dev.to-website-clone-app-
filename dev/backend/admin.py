from django.contrib import admin
from django.db import  models
from martor.widgets import AdminMartorWidget
from .models import Post,Like,Dislikes,AccountType,UserMembership
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':AdminMartorWidget}
    }

admin.site.register(Post,PostModelAdmin)
admin.site.register(Like)
admin.site.register(Dislikes)
admin.site.register(User,UserAdmin)
admin.site.register(AccountType)
admin.site.register(UserMembership)