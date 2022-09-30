from platform import release
from django.shortcuts import render, redirect, HttpResponse
from .models import *


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


def update_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        'page_title': 'Update',
        'show': show,
        'release_date': release_date,
        'form_title': 'Edit Show' + ' ' + str(show_id) + ': (' + show.title + ')',
        'form_action': '',       # giving an empty action will submit the form
                                 # to the same page that got us here(shows/<int:show_id>/edit)

    }
    if request.POST:  # i had to check because im using the same function to edit in the database and also to render the form
        show.title = request.POST['show_title']
        show.network = request.POST['show_network']
        show.release_date = request.POST['show_release_date']
        show.description = request.POST['show_description']
        show.save()
        return redirect('/shows/' + str(show.id))
    return render(request, "show_form.html", context)


def add_show(request):
    # i did this because if someone tried to enter the url from typing it in the browser.
    if request.POST:
        show_title = request.POST['show_title']
        show_network = request.POST['show_network']
        show_release_date = request.POST['show_release_date']
        show_desc = request.POST['show_description']
        show = TvShow.objects.create(
            title=show_title, network=show_network, release_date=show_release_date, description=show_desc)
        return redirect('/shows/' + str(show.id))
    return redirect('/shows')


def view_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    context = {
        'show': show,
        'page_title': 'Read (' + show.title + ')',
    }
    return render(request, "view_show.html", context)


def delete_show(request, show_id):
    show = TvShow.objects.get(id=show_id)
    show.delete()
    return redirect('/')
