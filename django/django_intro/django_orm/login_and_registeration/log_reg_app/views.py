from email import contentmanager
from django.shortcuts import render, redirect
from .models import *
from . import models
from django.contrib import messages


def root(request):
    return render(request, 'register.html')


def regist_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=first_name, last_name=last_name, email=email, password=password)
        messages.success(request, "Successfuly registered!")
        request.session['user_id'] = user.id
        return redirect('/success')


def success(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    return render(request, 'success.html', context)


def login(request):
    return render(request, 'login.html')
