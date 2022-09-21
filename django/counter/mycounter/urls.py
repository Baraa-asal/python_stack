from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_counter),
    path('reset', views.reset),
    path('add-two', views.add_two),
    path('count', views.specify_counter),
]

