from django.db import models
from authors.models import *


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    authors = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
