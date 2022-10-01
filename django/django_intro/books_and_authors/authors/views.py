from multiprocessing import context
from django.shortcuts import render, redirect

from books.models import Book
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
    author = Author.objects.get(id=author_id)
    context = {
        'author': author,
        'all_books': Book.objects.all(),
    }
    return render(request, 'author_details.html', context)


def add_author_to_book(request, book_id):
    # what is sent here in the POST is the option value but i catch it using the select name
    author_id = request.POST['add_author_to_book']
    book = Book.objects.get(id=book_id)
    book.authors.add(Author.objects.get(id=author_id))
    return redirect('/books/'+str(book_id))
