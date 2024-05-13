from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from comments import views

urlpatterns = [
    path('<int:post_id>/',views.comments_api_view, name = 'view-comment'), 
    path('<int:comment_id>/comment_id/',views.comments_delete_api_view,name='view-comment_id'), 
]

# 간소화 하기 