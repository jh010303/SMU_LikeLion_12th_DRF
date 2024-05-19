from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from posts import views

urlpatterns = [ 
    #path('',views.post_list_api_view, name='post-list'), # post 목록 조회, 생성
    #path('<int:post_id>/',views.post_retrieve_api_view,name = 'post-retrieve'), # post 단일 목록 조회,삭제,수정
    path('',views.PostListAPIView.as_view(),name = "post-list"),
    path('<int:post_id>/',views.PostRetrieveAPIView.as_view(),name = 'post-retrieve'), 
]

# ex) 127.0.0.1:8000/posts/이면 views파일에 post_list_api_view 실행하게 됨
# ex) 127.0.0.1:8000/posts/post_id/이면 views파일에 post_retrieve_api_view 실행하게 됨