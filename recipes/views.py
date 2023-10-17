from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    """return HTTP response"""
    return HttpResponse("Home 2")


def contact(request):
    """return HTTP response"""
    return HttpResponse("contact")


def about(request):
    """return HTTP response"""
    return HttpResponse("about")
    # return HTTP response
