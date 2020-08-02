from ..models import Post,Like,Dislikes,AccountType,FriendRequest
from ..serializers.serializers import FriendRequestSerializer,UserSerializer,PostSerializer,LikeSerializer,DislikesSerializer,AccountSerializer,RegisterSerilizer,LoginSerializer
from datetime import datetime
from rest_framework import generics,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import get_user_model
# from ..useserializers import RegisterSerilizer,LoginSerializer,UserSerilizer
User = get_user_model()