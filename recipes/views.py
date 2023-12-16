"""
My Views
render ->> read a file and render, return HttpResponse
"""

from django.shortcuts import render
from utils.recipes.factory import make_recipe
# Create your views here.


def home(request):
    """return HTTP response ->> render"""
    # return HttpResponse("Home 2")
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],  # {{name}}
    })


def recipe(request, id):
    """return HTTP response ->> render"""
    # return HttpResponse("Home 2")
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),  # {{name}}
    })
