from users.models import User 
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# 게시글 수정, 게시글 삭제
    
@api_view(['POST'])
def user_join_api_view(request): # user가 회원가입 하는 함수
    if request.method == 'POST': # 요청한 데이터를 생성해야 함
        # 회원가입에 필요한 데이터 가져옴 
        id = request.data.get('id')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        introducing = request.data.get('introdcuing')
        gender = request.data.get('gender')
        # 위의 데이터를 바탕으로 새로운 user model 생성
        new_user = User.objects.create_user(
            id=id,
            username=username,
            email = email,
            password = password,
            introducing = introducing,
            gender = gender
        )
        new_user.save() # 모델 저장
        serializer = UserSerializer(new_user) # 새로운 user 시리얼화
        serializer.save() # 저장
        return Response(serializer.data,status=status.HTTP_201_CREATED) # 새로운 user 반환

@api_view(['DELETE'])
def user_delete_api_view(request,pk): #user 삭제 ( 탈퇴 개념 )
    try:
        delete_user = User.objects.get(pk=pk)
    except delete_user.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE': 
        delete_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def user_login_api_view(request):
    # 사용자가 입력한 것
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.get(username = username) # 사용자가 입력한게 존재하는지
    
    # 사용자가 입력한 username에 따른 password가 있는지
    if not check_password(password,user.password): #암호화된 password와 복호화된 user.password 비교
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    token = RefreshToken.for_user(user) # user에게 token 발급, 토큰 주는 함수는 이거 말고도 많음
    # refreshtoken은 access_token을 갱신 하는 역할
    serializer = UserSerializer(user) # user 시리얼화
    return Response(
        status=status.HTTP_200_OK,
        data={
            "token":str(token.access_token), # token.access_token을 줌 -> login을 할 때 인증을 하는 token
            "user":serializer.data, # 유저 정보 줌
        }
    )

@api_view(['GET'])
def test_login(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user) # request.user 객체 ( 딕셔너리 형태 아님 )
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED) # 토큰 없이 보내면


    


        
        


        




    
        

    