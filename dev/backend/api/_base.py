from ..models import Post,Like,Dislikes
from ..serializers.serializers import PostSerializer,LikeSerializer,DislikesSerializer

from rest_framework import generics
from rest_framework.views import APIView