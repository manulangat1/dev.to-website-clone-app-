from ._base import *
class PostAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer