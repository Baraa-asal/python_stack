from multiprocessing import context
from pickletools import read_uint1
from typing import ContextManager
from django.shortcuts import redirect, render
from log_reg_app.models import User
from fav_books_app.models import Book
from .models import *


def root(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'all_books': Book.objects.all(),
    }
    return render(request, 'books.html', context)


def add_book_to_database(request):
    book_title = request.POST['book_title']
    book_description = request.POST['book_description']
    book_uploaded_by = User.objects.get(id=request.session['id'])
    book = Book.objects.create(title=book_title,
                               description=book_description,
                               uploaded_by=book_uploaded_by)
    book.users_who_like.add(User.objects.get(id=request.session['id']))

    return redirect('/books')


def add_book_to_favorites(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])
    book.users_who_like.add(user)
    return redirect('/books')

def view_or_update(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'view_or_update.html', context)