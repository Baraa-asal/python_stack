from ssl import create_default_context
from django.db import models
from log_reg_app.models import *


class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name='messages', on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(
        Message, related_name='comments_message', on_delete=models.CASCADE)
