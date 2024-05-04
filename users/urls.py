from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

from posts import views

urlpatterns = [
    path('',views.post_list_api_view, name='post-list'),
    path('<int:post_id>/',views.post_retrieve_api_view,name = 'post-retrieve')
]