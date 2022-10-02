from unittest.util import _MAX_LENGTH
from django.db import models


class TvShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['show_title']) < 2:
            errors["title"] = "Title should be at least 2 characters."
        if len(postData['show_network']) < 3:
            errors["network"] = "Network should be at least 3 characters."
        if len(postData['show_description']) < 10:
            errors["description"] = "Description should be at least 10 characters."
        return errors


class TvShow(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TvShowManager()
