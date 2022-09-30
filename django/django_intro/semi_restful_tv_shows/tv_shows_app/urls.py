from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows/', views.index),
    path('shows/new/', views.create_new_show),
    path('shows/create_show/', views.add_show),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/delete', views.delete_show),
    path('shows/<int:show_id>/edit', views.update_show),
]
