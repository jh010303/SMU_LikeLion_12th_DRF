from rest_framework import serializers
from posts.serializers import PostSerializer
from users.serializers import UserSerializer
from postlikes.models import PostLike

class commentsSerializer(serializers.ModelSerializer):
    post = PostSerializer() # pk-post 시리얼라이저
    user = UserSerializer() # pk-user 시니얼라이저

    class Meta:
        model = PostLike
        fields = ['post','user'] # '__all__' 모든 필드를 시리얼라이징 할 때 
