"""."""
from django.urls import path

from recipes.views import home, contact, about


# dominio/recipes -> home
urlpatterns = [
    path('', home),  # Home
    path('about/', about),  # /about/
    path('contact/', contact),  # /contact/
]
