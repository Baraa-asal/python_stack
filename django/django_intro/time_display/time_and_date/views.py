from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        "date": datetime.now().strftime('%b %d, %Y'),
        "time": datetime.now().strftime("%I:%M %p")
    }
    return render(request, 'index.html', context)
