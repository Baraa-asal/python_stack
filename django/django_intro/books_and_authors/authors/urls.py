from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('authors', views.index),
    path('authors/add_author', views.add_new_author),
    path('authors/<int:author_id>', views.view_author_details),
    path('authors/<int:book_id>/add_author_to_book', views.add_author_to_book),
]
