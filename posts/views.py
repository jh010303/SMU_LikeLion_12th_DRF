from posts.models import Post
from users.models import User
from posts.serializers import PostSerializer
from users.serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# 게시글 수정, 게시글 삭제

@api_view(['GET','POST'])
def post_list_api_view(request): # post 목록 조회
    if request.method == 'GET': # 요청된 정보를 검색하여 응답해줌 ( read )
        posts = Post.objects.all() # 포스트 전체
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # 요청된 자원을 생성(create)함 안 됨..
        serializer = PostSerializer(data=request.data) # 요청 데이터에 기반하여 PostSerializer 생성, PostSerailizer의 매개변수에는 딕셔너리
        # request.data: user가 작성한 게시글의 데이터, 처음 선언할 때 매개변수 1개만 넣어야 함
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE']) #patch 추가
def post_retrieve_api_view(request,post_id): # post 특정 목록 조회 (pk통해서 구분), pk에는 <int:post_id>가 옴
    # pk를 가진 post가 존재하는지 확인
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET': # ( 특정 게시글 read )
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT': # 요청된 자원을 수정(update)함, 전체 수정
        serializer = PostSerializer(post,data=request.data) # user의 모든 정보를 받음
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE': # 특정 게시글 삭제(delete)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    
        

    