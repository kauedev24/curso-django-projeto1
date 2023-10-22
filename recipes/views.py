"""
My Views
render ->> read a file and render, return HttpResponse
"""

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    """return HTTP response ->> render"""
    # return HttpResponse("Home 2")
    return render(request, 'recipes/home.html')


def contact(request):
    """return HTTP response"""
    return HttpResponse("contact")


def about(request):
    """return HTTP response"""
    return HttpResponse("about")
    # return HTTP response
