from django.db import models
from comments.models import Comment
from users.models import User

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name = 'commentlikes_from_comment', null= True);
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name = 'commentlikes_from_user',null=True);
