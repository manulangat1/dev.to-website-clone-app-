from ..models import Post,Like,Dislikes,AccountType,FriendRequest
from ..serializers.serializers import FriendRequestSerializer,UserSerializer,PostSerializer,LikeSerializer,DislikesSerializer,AccountSerializer
from datetime import datetime
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()