from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *


def root(request):
    return redirect('/authors')


def index(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)


def add_new_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    author_notes = request.POST['author_notes']
    Author.objects.create(first_name=first_name,
                          last_name=last_name, notes=author_notes)

    return redirect('/authors')


def view_author_details(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id)
    }
    return render(request, 'author_details.html', context)
