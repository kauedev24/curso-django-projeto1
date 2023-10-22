"""My Views"""

from django.http import HttpResponse
# from django.shortcuts import render

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
