from django.db import models
from log_reg_app.models import *

# class BookManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}

#         if len(postData['book_description']) < 5:
#             errors['first_name'] = "First name should be at least 2 characters!"

#         return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name='books_uploaded',
                                    on_delete=models.CASCADE)
    # the user who upladed a given book
    users_who_like = models.ManyToManyField(User, related_name='liked_books') #(this is new table)
    # a list of users who like a given book
    # objects = UserManager()
