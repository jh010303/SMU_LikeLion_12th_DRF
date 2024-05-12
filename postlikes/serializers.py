from rest_framework import serializers
from posts.serializers import PostSerializer
from users.serializers import UserSerializer
from postlikes.models import PostLike

class PostLikeSerializer(serializers.ModelSerializer):
    post = PostSerializer(required = False) # pk-post 시리얼라이저
    user = UserSerializer(required = False) # pk-user 시니얼라이저

    class Meta:
        model = PostLike
        fields = ['id','post','user'] # '__all__' 모든 필드를 시리얼라이징 할 때 
