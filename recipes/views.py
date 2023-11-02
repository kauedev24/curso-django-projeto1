"""
My Views
render ->> read a file and render, return HttpResponse
"""

from django.shortcuts import render

# Create your views here.


def home(request):
    """return HTTP response ->> render"""
    # return HttpResponse("Home 2")
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Kaue Oliveira'
    })
