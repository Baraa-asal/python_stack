from django.shortcuts import render, redirect
import random


def index(request):
    if 'gold' in request.session:
        del request.session['gold']
    return redirect("/gold")


def gold(request):
    return render(request, 'index.html')


def check_gold(request):
    source = ['farm', 'cave', 'house']
    if 'gold' not in request.session:
        request.session['gold'] = 0

    if request.POST['source'] in source:
        random_num = random.randint(10, 21)
        request.session['gold'] += random_num

    if request.POST['source'] == 'quest':
        random_num = random.randint(-50, 50)
        request.session['gold'] += random_num

    return redirect("/gold")
