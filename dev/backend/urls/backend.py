from ._base import *

urlpatterns = [
    path('',PostAPI.as_view(),name="posts")
]