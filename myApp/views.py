from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import Country
from django.views.decorators.http import require_GET



def countryautocomplete(request):
    query = request.GET.get('q', '')
    countries = Country.objects.filter(name__icontains=query).values('name')
    return JsonResponse(list(countries), safe=False)


def home(request):
    return render(request, 'home.html')