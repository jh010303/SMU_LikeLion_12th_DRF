from rest_framework import serializers
from users.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField() # 파라미터에 옵션 read_only, write_only

    class Meta:
        model = User
        fields = ['id','username','email', 'password', 'posts_num'] # '__all__' 모든 필드를 시리얼라이징 할 때, 이 때는 리스트 사용 X
        extra_kwargs = {'password':{'write_only':True}}
    
    def get_posts_num(self,obj):
        return Post.objects.filter(user=obj).count()
    