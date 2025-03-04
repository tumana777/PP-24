from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car
from .forms import CarForm

def index(request):

    cars = Car.objects.all().select_related('category')

    return render(request, 'index.html', {'cars': cars})

def about(request):

    return render(request, 'about.html')

def car_details(request, car_pk):

    car = get_object_or_404(Car, pk=car_pk)

    return render(request, 'car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        print(request.method)
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = CarForm()

    print(request.method)

    return render(request, 'add_car.html', {'form': form})