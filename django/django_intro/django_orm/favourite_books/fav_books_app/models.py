from django.db import models
from log_reg_app.models import *


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='books',
                             on_delete=models.CASCADE)
    fav_books = models.ManyToManyField(User, related_name='fav_books')
