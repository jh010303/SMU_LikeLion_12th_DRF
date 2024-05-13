from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from users import views

urlpatterns = [
    path('',views.user_join_api_view,name='user-join'), # 도메인주소/users/login/이면 view의 user_join_api_view 함수 실행, 회원가입
    path('login/',views.user_login_api_view,name='user-login'), # 도메인주소/users/이면 view의 user_login_api_view 함수 실행, 로그인
    path('<int:user_id>/',views.user_delete_api_view,name='user-delete'), # 도메인주소/users/delete/이면 view의 user_delete_api_view 함수 실행, 회원탈퇴
    path('test/',views.test_login,name='user-test'),
]
#join -> 빈칸으로 두고, 
# delete -> id
# 동사를 앵간하면 안 씀