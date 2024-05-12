from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from comments import views

urlpatterns = [
    path('<int:post_id>/',views.comments_api_view, name = 'view-comment'),
    path('create/<int:post_id>/',views.create_comments_api_view,name='create-comment'), 
    path('delete/<int:comment_id>/',views.comments_delete_api_view,name='delete-comment'), 
    path('update/<int:comment_id>/',views.comments_update_api_view,name='update-comment'), 
]
