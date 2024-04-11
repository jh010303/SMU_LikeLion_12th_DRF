from rest_framework import serializers
from users.serializers import UserSerializer
from postlikes.models import PostLike
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer() # pk 시리얼라이저
    postlikes_num = serializers.SerializerMethodField() # 게시글의 좋아요 개수

    class Meta:
        model = Post
        fields = ['title','content','user'] # '__all__' 모든 필드를 시리얼라이징 할 때 

    def get_postlikes_num(self,obj): # 게시글의 좋아요 개수 반환
        return PostLike.objects.filter(user=obj).count()
    
    
