from django.db import models 
from django.contrib.auth.models import AbstractUser
from users.models import User

# models를 사용하면 id는 자동 생성
class Post(models.Model): # 일 대 다 에서 다쪽, PK를 가지고 있음
    title = models.CharField(max_length=50,null=True)# 보통 많이 사용
    content = models.CharField(max_length=100,null=True,blank=True) # 빈칸 허용
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'posts',null=True)
