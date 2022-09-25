from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('gold/', views.gold),
    path('gold/earn_or_lose/', views.check_gold),
]
