
from ._base import * 

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = (
            'id',
            'user',
            'type',
            'created',
            'valid_through'
        )
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'friends'
        )
class UserSerializer(serializers.ModelSerializer):
    friends = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'friends'
        )
    def get_friends(self,obj):
        return UsersSerializer(obj.friends.all(),many=True).data
class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = (
            'id',
            'to_user',
            'from_user',
        )
class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'published_at',
            'updated_at',
            'likes',
            'dislikes'
        )
    def get_likes(self,obj):
        return obj.get_likes_all()
    def get_dislikes(self,obj):
        return obj.get_dislikes_all()
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'id',
            'post',
            'likes'
        )

class DislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislikes
        fields = (
            'id',
            'post',
            'dislikes'
        )