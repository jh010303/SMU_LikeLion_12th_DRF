from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from postlikes import views

urlpatterns = [
    path('<int:post_id>/',views.postlikes_list_api_view, name='view-postlikes'), # 특정 게시글의 좋아요 보기
    path('create/<int:post_id>/',views.create_postlikes_api_view,name = 'create-postlikes'), # 특정 게시글의 좋아요 달기
    path('delete/<int:postlikes_id>/',views.delete_postlikes_api_view,name = 'delete-postlikes'), # 특정 게시글의 좋아요 삭제  
]