from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def result(request):
    context = {
        'info': request.POST
    }
    return render(request, "result.html", context)
