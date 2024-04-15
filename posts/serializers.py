from rest_framework import serializers
from users.serializers import UserSerializer
from postlikes.models import PostLike
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer() # fk user
    postlikes_num = serializers.SerializerMethodField() # 게시글의 좋아요 개수

    class Meta:
        model = Post
        fields = ['id','title','content','user','created_at','updated_at','postlikes_num']
        extra_kwargs = {'created_at':{'read_only':True}} # 만들어진 시간은 고칠 수 없게

    def get_postlikes_num(self,obj): # 게시글의 좋아요 개수 반환
        return PostLike.objects.filter(post=obj).count()
        # 게시글의 좋아요 개수
        # 특정 게시글의 serializer
    
    
