
from django.db import models
# import bcrypt


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters!"
        if not (postData['first_name']).isalpha():
            errors['first_name'] = "Please use only letters, try again!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters!"
        if not (postData['last_name']).isalpha():
            errors['last_name'] = "Please use only letters, try again!"
        if len(postData['email']) < 2:
            errors['email'] = "Please enter a valid email!"
        if len(postData['password']) < 8:
            errors['password'] = "Passoword should be at least 8 characters!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
