from django.urls import path
from myApp.views import *

urlpatterns = [
    path('country-autocomplete/', countryautocomplete, name='countryautocomplete'),
    path('', home, name='home'),
]
