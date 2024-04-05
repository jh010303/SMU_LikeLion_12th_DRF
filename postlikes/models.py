from django.db import models
from posts.models import Post
from users.models import User

class PostLike(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name = 'postlikes_from_post',null=True);
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'postlikes_from_user',null=True);