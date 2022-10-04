from multiprocessing import context
from django.shortcuts import render, redirect
from . models import *


def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }
    return render(request, 'index.html', context)


def add_dojo(request):
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['dojo_state']

    Dojo.objects.create(
        name=name,
        city=city,
        state=state
    )
    return redirect('/')


def add_ninja(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo_id = request.POST['dojo']
    print(dojo_id)
    Ninja.objects.create(
        first_name=first_name,
        last_name=last_name,
        dojo=Dojo.objects.get(id=dojo_id)
    )
    return redirect('/')


def delete_tables(request):
    Dojo.objects.all().delete()
    Ninja.objects.all().delete()
    return redirect("/")
