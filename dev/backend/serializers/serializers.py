
from ._base import * 



from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password =  serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        return serializers.ValidationError("Incorect Credential")
        # return super().validate(attrs)

# register serializers
class RegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'bio'
        )
        extra_kwargs={'password':{'write_only':True}}
    def create(self, validated_data):
        # return super().create(validated_data)
        t = True
        user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
        user.bio = validated_data['bio']
        user.save()
        return user
# user serializer
# class UserSerilizer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'id',
#             'username',
#             'email',
#             'tel_no',
#             'bio',
#             'friends'
#         )

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
            'bio',
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
            'bio',
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