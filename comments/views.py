from posts.models import Post
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# 게시글에 댓글 달기
# 게시글의 댓글 보기 ( 누가 적었는지 ?)

# Create your views here.
@api_view(['GET','POST']) 
def comments_api_view(request,post_id): # 특정 게시글에 댓글 보기
    try: # 특정 게시글 찾기
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': # 댓글 보기
        comments = Comment.objects.filter(post = post) # 특정 게시글의 댓글 찾기
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST': # 댓글 생성
        serializer = CommentSerializer(data = request.data) # 입력 데이터, user 채워주기
        # serializer에 post가 빠져 있음
        if serializer.is_valid():
            serializer.save(post = post, user = request.user) # serializer에 post 채워주기
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def comments_delete_api_view(request,comment_id): # 특정 게시글의 특정 댓글 삭제
    try: # 특정 댓글 찾기
        comment = Comment.objects.get(id=comment_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE': # 댓글 삭제
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT': # 댓글 수정
        serializer = CommentSerializer(comment,data=request.data) # comment 데이터 수정
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)