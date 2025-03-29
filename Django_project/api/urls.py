from .views import car_list
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('cars/', car_list, name='car_list'),
]