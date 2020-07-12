from ._base import *
class PostAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class DislikesAPI(generics.ListAPIView):
    queryset = Dislikes.objects.all()
    serializer_class = DislikesSerializer