from django.db import models
from users.models import User

class Follow(models.Model):
    follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'follow_from_er',null=True);
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'follow_from_ing',null=True);
