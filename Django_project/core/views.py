from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Category
from .forms import CarForm

def index(request):

    search_query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    year = request.GET.get('year', '')
    max_year = request.GET.get('max_year', '')

    cars = Car.objects.all().select_related('category')

    if search_query:
        cars = cars.filter(Q(make__icontains=search_query) | Q(model__icontains=search_query))

    if category:
        cars = cars.filter(category_id=category)

    if year:
        cars = cars.filter(year__gte=year)

    if max_year:
        cars = cars.filter(year__lte=max_year)

    categories = Category.objects.all()

    return render(request, 'index.html', {
        'cars': cars,
        'categories': categories,
        'search_query': search_query,
        'category': category,
        'year': year,
        'max_year': max_year,
    })

def about(request):

    return render(request, 'about.html')

def car_details(request, car_pk):

    car = get_object_or_404(Car, pk=car_pk)

    return render(request, 'car_detail.html', {'car': car})

def add_car(request):
    if request.method == 'POST':
        print(request.method)
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = CarForm()

    print(request.method)

    return render(request, 'add_car.html', {'form': form})

def update_car(request, car_pk):
    car = get_object_or_404(Car, pk=car_pk)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)

        if form.is_valid():
            form.save()
            return redirect('core:car_details', car_pk=car.pk)

    else:
        form = CarForm(instance=car)

    return render(request, 'car_update.html', {'form': form})