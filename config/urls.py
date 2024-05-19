"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('posts/', include('posts.urls')), 
    path('', include('users.urls')),  # viewset 사용
    path('comments/', include('comments.urls')), 
    path('postlikes/', include('postlikes.urls')), 
    path('commentlikes/', include('commentlikes.urls')), 
]
#urlpatters에 첫번째 매개변수 route:str은 주소뒤에 오는 것
# ex) 127.0.0.1:8000/posts/  ?   에서 ?은 posts.urls.py에서 처리하게 됨

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
