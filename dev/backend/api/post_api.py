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

class UserAPI(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # def get_object(self):
    #     return self.request.user

class FriendRequestCreateAPI(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def perform_create(self, serializer):
        return serializer.save(updated_at=datetime.now())
class FriendRequestAccept(APIView):
    def post(self,request,*args,**kwargs):
        pk = kwargs['pk']
        friendR = FriendRequest.objects.get(pk=pk)
        print(friendR)
        user1 = request.data['to_user']
        user2 = request.data['from_user']
        print(user1,user2)
        User1 = User.objects.get(pk=user1)
        User2 = User.objects.get(pk=user2)
        print(User1,User2)
        User1.friends.add(User2)
        User2.friends.add(User1)
        return Response("hey")