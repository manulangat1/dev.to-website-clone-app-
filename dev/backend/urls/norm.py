from ._base import * 
from ..views import index
urlpatterns = [
    path('',index,name="posts"),
    # path('likes/',LikeAPI.as_view(),name="like"),
    # path('dislikes/',DislikesAPI.as_view(),name="dislikes")
]