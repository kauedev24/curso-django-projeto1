"""."""
from django.urls import path

from recipes.views import home


# dominio/recipes -> home
urlpatterns = [
    path('', home),  # Home
]
