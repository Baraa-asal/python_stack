from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('books', views.index),
    path('books/add_book', views.add_new_book),
    path('books/<int:book_id>', views.view_book_details),
]
