from users.models import User 
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.decorators import action
from users.permissions import IsOwner

class UserViewSet(viewsets.ModelViewSet): # 사용자 탈퇴는 권환이 있어야 함
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'user_id' 
    permission_classes = [IsOwner] 

    @action(methods=['POST'],detail = False, url_path='login',url_name='user-login')
    def login(self,request): # 로그인
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username = username) 
        if not check_password(password,user.password): 
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        token = RefreshToken.for_user(user) 
        serializer = UserSerializer(user) 
        return Response(
            status=status.HTTP_200_OK,
            data={
                "token":str(token.access_token), 
                "user":serializer.data,
            }
        )
    
    @action(methods=['GET'],detail = False, url_path='test',url_name='test-login')
    def test(self,request): 
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)