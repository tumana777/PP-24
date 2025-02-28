from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Car

def index(request):

    cars = Car.objects.all()

    return render(request, 'index.html', {'cars': cars})

def about(request):

    return render(request, 'about.html')