from rest_framework import serializers
from comments.serializers import CommentSerializer
from users.serializers import UserSerializer
from commentlikes.models import CommentLike

class CommentLikeSerializer(serializers.ModelSerializer):
    comment = CommentSerializer() # fk-comment 
    user = UserSerializer() # fk-user 

    class Meta:
        model = CommentLike
        fields = ['id','comment','user']
