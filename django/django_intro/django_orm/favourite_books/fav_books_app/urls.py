from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('add_book/', views.add_book_to_database),
    path('add_book_to_favorites/<int:book_id>', views.add_book_to_favorites),
    path('view_or_update/<int:book_id>', views.view_or_update),
]
