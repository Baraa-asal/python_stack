from django.shortcuts import render, HttpResponse	# notice the import!
from django.http import JsonResponse


def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)


def root(request):
    return redirect('/blogs')
