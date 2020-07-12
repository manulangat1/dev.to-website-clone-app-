
from ._base import * 

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'published_at',
            'updated_at'
        )
