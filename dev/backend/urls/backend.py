from ._base import *

urlpatterns = [
    path('',PostAPI.as_view(),name="posts"),
    path('likes/',LikeAPI.as_view(),name="like"),
    path('dislikes/',DislikesAPI.as_view(),name="dislikes")
]