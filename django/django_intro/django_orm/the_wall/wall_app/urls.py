from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('create_message', views.create_message),
    path('create_comment', views.create_comment),
    path('delete_message', views.delete_message),
]
