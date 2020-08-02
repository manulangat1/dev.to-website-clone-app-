from django.urls import path
from django.urls import path,include
from  ..api.post_api import PostAPI,LikeAPI,DislikesAPI,AccountAPI,UserAPI,FriendRequestAccept,FriendRequestCreateAPI,FriendRequestUnfollow,PostDetailsAPI,LikeCreateAPI,UserAPI,RegisterAPI,LoginAPI,FriendRequestList
from knox import views as knox_views