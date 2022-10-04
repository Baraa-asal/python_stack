from django.shortcuts import render, redirect

# Create your views here.


def root(request):
    return redirect('/books')


def index(request):
    return redirect()
