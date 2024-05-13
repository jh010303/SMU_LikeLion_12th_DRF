from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from postlikes.models import PostLike
from postlikes.serializers import PostLikeSerializer
from posts.models import Post

# 특정 게시글의 좋아요 달기 ( 유저 당 1개 )
# 특정 게시글의 좋아요 개수 보기 -> 특정 게시글
# 누가 좋아요 눌렀는지 보기
# Create your views here

@api_view(['GET','POST']) 
def postlikes_list_api_view(request,post_id): # 특정 게시글의 좋아요 보기
    try: # 특정 게시글 찾기
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': # 특정 게시글에 있는 좋아요 보기
        postlikes = PostLike.objects.filter(post = post) # 특정 게시글에 있는 좋아요 보기 
        serializer = PostLikeSerializer(postlikes,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST': # 특정 게시글에 좋아요 달기
        postlike = PostLike.objects.create(user = request.user, post = post) # request.data에 아무것도 없을 때는 create 사용,object manager로 사용
        serializer = PostLikeSerializer(postlike)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) 
def delete_postlikes_api_view(request,postlikes_id): # 특정 게시글의 좋아요 보기
    try: # 특정 게시글 찾기
        postlikes = PostLike.objects.get(id = postlikes_id)
    except PostLike.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        postlikes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)