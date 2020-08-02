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
    pic = serializers.ImageField(default=None)
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
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'tel_no',
            'bio',
            'friends'
        )