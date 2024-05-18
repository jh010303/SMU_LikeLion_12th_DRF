from rest_framework import serializers
from users.serializers import UserSerializer
from postlikes.models import PostLike
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required = False) # fk user 실제 앱에서는 post가 생성되면 당연히 user가 필요함 -> 일단 임시로..
    postlikes_num = serializers.SerializerMethodField() # 게시글의 좋아요 개수
    #serializers.SerializerMethodField의 매개변수에는 함수 이름이 들어간다. 
    #default로 설정하면 get_변수명으로 설정된다.
    #=> def 함수 이름 설정 중요 !!!

    class Meta:
        model = Post
        fields = ['id','title','content','user','created_at','updated_at','postlikes_num']
        extra_kwargs = {'created_at':{'read_only':True}} # 만들어진 시간은 고칠 수 없게

    def get_postlikes_num(self,obj): # 게시글의 좋아요 개수 반환
        return PostLike.objects.filter(post=obj).count()
        # 게시글의 좋아요 개수
        # 특정 게시글의 serializer