from ._base import *

urlpatterns = [
    path('',PostAPI.as_view(),name="posts"),
    path('user/<pk>/',UserAPI.as_view(),name="user"),
    path('friend/',FriendRequestCreateAPI.as_view(),name="user"),
    
    path('friend/<pk>/',FriendRequestAccept.as_view(),name="user"),
    path('unfriend/<pk>/',FriendRequestUnfollow.as_view(),name="user_unfollow"),
    path('likes/',LikeAPI.as_view(),name="like"),
    path('accounts/',AccountAPI.as_view(),name="like"),
    path('dislikes/',DislikesAPI.as_view(),name="dislikes")
]