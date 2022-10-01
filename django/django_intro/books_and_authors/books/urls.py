from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('books', views.index),
    path('books/add_book', views.add_new_book),
    path('books/<int:book_id>', views.view_book_details),
    path('books/<int:author_id>/add_book_to_author', views.add_book_to_author),

]
