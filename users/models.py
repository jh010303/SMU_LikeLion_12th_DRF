from django.db import models 
from django.contrib.auth.models import AbstractUser

# models를 사용하면 id는 자동 생성
class User(AbstractUser):
    introducing = models.CharField(max_length=10,null=True,blank=True)
    gender = models.CharField(max_length=2, null=True)


