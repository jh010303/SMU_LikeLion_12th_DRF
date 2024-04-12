from rest_framework import serializers
from posts.serializers import PostSerializer
from users.serializers import UserSerializer
from commentlikes.models import CommentLike
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer() # fk-post 
    user = UserSerializer() # fk-user 

    commentlike_num = serializers.SerializerMethodField() # 댓글 좋아요 개수
    
    class Meta:
        model = Comment
        fields = ['id','post','user','content']

    def get_commentlike_num(self,obj): # 댓글 좋아요 개수 반환
        return CommentLike.objects.filter(CommentLike=obj).count()
