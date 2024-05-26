from posts.models import Post
from users.models import User
from posts.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from posts.permissions import IsOwnerOrReadOnly

class PostListAPIView(ListCreateAPIView): # 게시글 생성, 조회 클래스
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    permission_class = [IsOwnerOrReadOnly]

    def create(self,request): 
        serializer = PostSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #def perform_create(self, serializer):
    #    serializer.save(user = request.user)
    # 위에꺼 지우고 perform_create만 해도 괜찮음

class PostRetrieveAPIView(RetrieveUpdateDestroyAPIView): # 게시글 삭제, 수정, 조회 클래스 ( 특정 게시글만 )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'post_id' # 특정 게시글의 id
    permission_classes = [IsOwnerOrReadOnly]
