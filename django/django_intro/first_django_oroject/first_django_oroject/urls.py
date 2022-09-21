from django.urls import path, include

urlpatterns = [
    path('/blogs', include('my_first_app.urls')),
]

