"""."""
from django.urls import path

from . import views


# dominio/recipes -> home
urlpatterns = [
    path('', views.home),  # Home
    path('recipes/<id>/', views.recipe),
]
