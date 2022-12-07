from django.shortcuts import render
from django.http import HttpResponse


def get_hello(request):
    return HttpResponse("<h1>Django app</h1>")


def index_page(request):
    return render(request, "index.html", {})

# Create your views here.
