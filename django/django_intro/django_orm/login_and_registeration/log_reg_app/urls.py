from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('register/', views.regist_user),
    path('login', views.login),
    path('success/', views.success),
]
