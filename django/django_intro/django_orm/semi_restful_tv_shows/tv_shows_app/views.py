from django.shortcuts import render, redirect, HttpResponse
from .models import *
from . import models
from django.contrib import messages


def root(request):
    return redirect('shows/')


def index(request):
    context = {
        'page_title': 'Read(All)',
        'shows': TvShow.objects.all()
    }
    return render(request, 'shows.html', context)


def create_new_show(request):
    context = {
        'page_title': 'Create',
        'form_title': 'Add a New Show',
        'form_action': '/shows/create_show/',
    }
    return render(request, "show_form.html", context)


def edit_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        'page_title': 'Update',
        'show': show,
        'release_date': release_date,
        'form_title': 'Edit Show' + ' ' + str(show_id) + ': (' + show.title + ')',
        'form_action': '/shows/' + str(show.id) + '/update',
    }
    return render(request, "show_form.html", context)


def update_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    errors = TvShow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(show.id)+'/edit')

    else:
        show.title = request.POST['show_title']
        show.network = request.POST['show_network']
        show.release_date = request.POST['show_release_date']
        show.description = request.POST['show_description']
        show.save()
        return redirect('/shows/' + str(show.id))


def add_show(request):
    errors = TvShow.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')
    else:
        # i did the if because if someone tried to enter the url from typing it in the browser.
        if request.POST:  
            show = models.createTvShow(request)
            return redirect('/shows/' + str(show.id))
        return redirect('/shows')

# This view will display the ....
def view_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    context = {
        'show': show,
        'page_title': 'Read (' + show.title + ')',
    }
    return render(request, "view_show.html", context)


def delete_show(request, show_id):
    models.deleteTVShow(show_id)
    return redirect('/')
