from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from postlikes import views

urlpatterns = [
    path('<int:post_id>/',views.postlikes_list_api_view, name='view-postlikes'), # 특정 게시글의 좋아요 보기, 생성
    path('<int:postlikes_id>/postlikes_id/',views.delete_postlikes_api_view,name = 'delete-postlikes'), # 특정 게시글의 좋아요 삭제  
]

# url 간소화 하기 위에 2개 묶기