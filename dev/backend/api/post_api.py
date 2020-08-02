from ._base import *




class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerilizer
    # parser_classes = (MultiPartParser, FormParser)
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)[1]
        })
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user

def infinite_filter(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    user = request.user
    print(user)
    return Post.objects.all()[int(offset):int(offset+limit)]

def is_there_more_data(request):
    offset = request.GET.get('offset')
    if int(offset) > Post.objects.all().count():
        return False
    return True
class PostAPI(generics.ListAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_queryset(self):
        qs = infinite_filter(self.request)
        return qs
    def list(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response({
            "posts":serializer.data,
            "has_more":is_there_more_data(request)
        })

class PostDetailsAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class LikeAPI(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
class LikeCreateAPI(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def post(self,request,*args,**kwargs):
        uses = 1 
        pos = request.data['id']
        # pos =request.POST.get('id')
        print(pos)
        user = User.objects.get(pk=uses)
        post  = Post.objects.get(pk=pos)
        like = Like.objects.filter(post=post,user=user)
        if user and post and like:
            print(like)
            like.delete()
            return Response("Like removed")
            
        else:
            likeS = Like.objects.create(user=user,post=post)
            likeS.likes = True 
            likeS.save()
            return Response("hey")
class DislikesAPI(generics.ListAPIView):
    queryset = Dislikes.objects.all()
    serializer_class = DislikesSerializer

class AccountAPI(generics.ListCreateAPIView):
    queryset = AccountType.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        return serializer.save(valid_through=datetime.now())

class FriendRequestCreateAPI(generics.ListCreateAPIView):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def perform_create(self, serializer):
        from_user=self.request.user
        to_id = self.request.data['to_user']
        updated_at=datetime.now()
        to_user = User.objects.get(pk=to_id)
        if to_user:
            return serializer.save(from_user=from_user,to_user=to_user,updated_at=updated_at)
        return Response("User does not exist")
class FriendRequestList(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def get_queryset(self):
        user = self.request.user
        print(user)
        friendr = FriendRequest.objects.filter(to_user=user).all()
        print(friendr)
        return friendr
class FriendRequestAccept(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def post(self,request,*args,**kwargs):

        pk = kwargs['pk']
        user = self.request.user
        friendR = FriendRequest.objects.get(pk=pk)
        # print(friendR)
        if friendR and friendR.to_user == user:
            from_user = friendR.from_user
            print(from_user)
            user.friends.add(from_user)
            from_user.friends.add(user)
            friendR.delete()
        return Response("hey")
class FriendRequestUnfollow(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    def post(self,request,*args,**kwargs):
        pk = kwargs['pk']
        friendR = FriendRequest.objects.get(pk=pk)
        if friendR:
            print(friendR)
            user1 = request.data['to_user']
            user2 = request.data['from_user']
            print(user1,user2)
            User1 = User.objects.get(pk=user1)
            User2 = User.objects.get(pk=user2)
            print(User1,User2)
            User1.friends.remove(User2)
            User2.friends.remove(User1)
        return Response("hey")
        