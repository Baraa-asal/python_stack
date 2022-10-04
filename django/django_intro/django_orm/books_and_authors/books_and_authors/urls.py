from django.urls import path, include

urlpatterns = [
    path('', include('books.urls')),
    path('', include('authors.urls')),
    path('/books', include('books.urls')),
    path('/authors', include('authors.urls')),
]
