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


def deleteTVShow(show_id):
    show = TvShow.objects.get(id=show_id)
    show.delete()

def createTvShow(request):
    show_title = request.POST['show_title']
    show_network = request.POST['show_network']
    show_release_date = request.POST['show_release_date']
    show_desc = request.POST['show_description']
    show = TvShow.objects.create(
        title=show_title, network=show_network, release_date=show_release_date, description=show_desc)
    return show


