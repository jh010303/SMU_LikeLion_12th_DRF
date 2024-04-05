from django.db import models
from users.models import User
from posts.models import Post

class Comment(models.Model):
    content = models.CharField(max_length=100,null=True,blank=False);
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'comments_from_user', null=True);
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'comments_from_post', null=True);



