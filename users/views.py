from users.models import User 
from users.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# 게시글 수정, 게시글 삭제
    
@api_view(['GET'])
def user_list_api_view(request): 
    if request.method == 'GET': # user 목록 조회
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def user_login_api_view(request): # user가 login 하는 view 함수
    if request.method == 'GET': # 데이터를 읽어야 함
        email = request.data.get('email') # email 입력 데이터 ( 로그인 할 때 사용 )
        password = request.data.get('password') # password 입력 데이터

        try: 
            user = User.objects.get(email=email) # 입력한 email과 매칭되는 user 모델 찾음
        except User.DoesNotExist: # 입력한 이메일이 없으면 404 출력
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        # 이메일이 존재하고 비밀번호가 맞으면
        if user.check_password(password):
            user.save() # user 모델 저장
            serializer = UserSerializer(user) # 요청하는 data에 대응하는 user 가져옴
            serializer.save() # 저장
            return Response(serializer.data) # user 반환
        
        # 비밀번호가 맞지 않으면
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
    


        
        


        




    
        

    