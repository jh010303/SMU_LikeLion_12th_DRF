from rest_framework import serializers
from comments.serializers import CommentSerializer
from users.serializers import UserSerializer
from commentlikes.models import CommentLike

class CommentLikeSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(required = False) # fk-comment 
    user = UserSerializer(required = False) # fk-user 

    class Meta:
        model = CommentLike
        fields = ['id','comment','user']
