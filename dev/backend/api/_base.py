from ..models import Post,Like,Dislikes,AccountType
from ..serializers.serializers import PostSerializer,LikeSerializer,DislikesSerializer,AccountSerializer
from datetime import datetime
from rest_framework import generics
from rest_framework.views import APIView