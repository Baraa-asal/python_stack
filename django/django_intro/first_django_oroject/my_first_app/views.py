from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse


def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse("Placeholder to later display a list of ALL blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a NEW blog")


def create(request):
    return redirect('/')


def show(request, num):
    return HttpResponse(f"Placeholder to display blog number : {num}")


def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")


def destroy(request, num):
    return redirect("/blogs")


def jsonResp(request):
    return JsonResponse({
                        "title": "My first blog",
                        "content": "Im happy to do this bonus."
                        })
