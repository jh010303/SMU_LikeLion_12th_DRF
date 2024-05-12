from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from comments import views

urlpatterns = [
    path('<int:post_id>/',views.comments_api_view, name = 'view-comment'),
    path('create/<int:post_id>/',views.create_comments_api_view,name='view-comment'), # 도메인주소/users/이면 view의 user_login_api_view 함수 실행\
    path('delete/<int:comment_id>/',views.comments_delete_api_view,name='view-comment'), # 도메인주소/users/이면 view의 user_login_api_view 함수 실행\
    path('update/<int:comment_id>/',views.comments_update_api_view,name='view-comment'), # 도메인주소/users/이면 view의 user_login_api_view 함수 실행\
]
