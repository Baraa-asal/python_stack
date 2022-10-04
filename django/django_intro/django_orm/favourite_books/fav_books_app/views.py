from django.shortcuts import redirect, render
from log_reg_app.models import User
# from fav_books_app.models import Book


def root(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
    }
    return render(request, 'books.html', context)
