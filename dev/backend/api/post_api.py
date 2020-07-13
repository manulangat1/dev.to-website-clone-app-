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

class AccountAPI(generics.ListCreateAPIView):
    queryset = AccountType.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        return serializer.save(valid_through=datetime.now())