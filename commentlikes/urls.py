from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings
from commentlikes import views

urlpatterns = [
    path('<int:comment_id>/',views.commentlikes_list_api_view, name='view-commentlikes'), # 특정 댓글의 좋아요 보기, 생성
    path('<int:commentlikes_id>/commentlikes_id/',views.delete_commentlikes_api_view,name = 'delete-commentlikes'), # 특정 댓글의 좋아요 삭제  
]