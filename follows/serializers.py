from rest_framework import serializers
from users.serializers import UserSerializer
from follows.models import Follow

class FollowSerializer(serializers.ModelSerializer):
    follower = UserSerializer() # fk user (follower)
    following = UserSerializer() # fk user (following)

    class Meta:
        model = Follow
        fields = ['id','follower','following']

    
    
