
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