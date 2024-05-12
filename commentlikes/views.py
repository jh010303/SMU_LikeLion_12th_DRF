from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from commentlikes.serializers import CommentLikeSerializer
from comments.models import Comment
from commentlikes.models import CommentLike

# 특정 게시글의 좋아요 달기 ( 유저 당 1개 )
# 특정 게시글의 좋아요 개수 보기 -> 특정 게시글
# 누가 좋아요 눌렀는지 보기
# Create your views here

@api_view(['GET']) 
def commentlikes_list_api_view(request,comment_id): # 특정 댓글의 좋아요 보기
    try: # 특정 댓글 찾기
        comment = Comment.objects.get(pk = comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        commentlikes = CommentLike.objects.filter(comment = comment) # 특정 댓글에 있는 좋아요 보기 
        serializer = CommentLikeSerializer(commentlikes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def create_commentlikes_api_view(request,comment_id): # 특정 댓글에 좋아요 달기
    try: # 특정 댓글 찾기
        comment = Comment.objects.get(pk = comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        serializer = CommentLikeSerializer(data = request.data) # 댓글 좋아요 만들기
        if serializer.is_valid():
            serializer.save(comment = comment) # 댓글 좋아요의 comment를 특정 comment로 
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['DELETE']) 
def delete_commentlikes_api_view(request,commentlikes_id): # 특정 댓글 좋아요 삭제하기
    try: # 특정 댓글 좋아요 찾기
        commentlikes = CommentLike.objects.get(pk = commentlikes_id)
    except CommentLike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        commentlikes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)