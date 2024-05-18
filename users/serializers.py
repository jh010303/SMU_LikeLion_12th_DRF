from rest_framework import serializers
from users.models import User
from posts.models import Post

class UserSerializer(serializers.ModelSerializer):
    posts_num = serializers.SerializerMethodField() # 게시글 숫자 

    class Meta:
        model = User
        fields = ['id','username','email', 'password', 'posts_num','introducing','gender'] # '__all__' 모든 필드를 시리얼라이징 할 때, 이 때는 리스트 사용 X
        extra_kwargs = {'password':{'write_only':True}}
        
    def get_posts_num(self,obj): # 게시글 숫자 반환
        return Post.objects.filter(user=obj).count()

    def create(self, validated_data): # user create 함수 재선언
        return User.objects.create_user(**validated_data)