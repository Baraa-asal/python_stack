from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *


def root(request):
    return redirect('/books')


def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)


def add_new_book(request):

    book_title = request.POST['book_title']
    book_desc = request.POST['book_description']
    Book.objects.create(title=book_title, description=book_desc)

    return redirect('/books')


def view_book_details(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'book_details.html', context)
