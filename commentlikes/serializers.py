from rest_framework import serializers
from comments.serializers import commentsSerializer
from users.serializers import UserSerializer
from commentlikes.models import CommentLike

class commentsSerializer(serializers.ModelSerializer):
    comment = commentsSerializer() # fk-comment 
    user = UserSerializer() # fk-user 

    class Meta:
        model = CommentLike
        fields = ['comment','user']
