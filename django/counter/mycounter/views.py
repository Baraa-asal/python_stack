from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render, redirect



# Create your views here.
def show_counter(request):
    if 'flag_h' in request.session and request.session['flag_h'] == 1:
        request.session['flag_h'] = 0

        if 'times' not in request.session:
            request.session['times'] = 0
            request.session['visits'] = 0
        else:
            request.session['times'] += 1
            
    else:
        if 'times' not in request.session:
            request.session['times'] = 0
            request.session['visits'] = 0
        else:
            request.session['visits'] += 1
            request.session['times'] += 1

    context = {
        'times': request.session['times'],
        'visits': request.session['visits'],
    }

    return render(request, 'index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')

def add_two(request):
    request.session['times'] += 1
    request.session['flag_h'] = 1
    return redirect('/')

def specify_counter(request):
    request.session['times'] += int(request.POST['count'])
    request.session['flag_h'] = 1
    context = {
        'times': request.session['times'],
        'visits': request.session['visits'],
        
    }
    return redirect('/')
    



