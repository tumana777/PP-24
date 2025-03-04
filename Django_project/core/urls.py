
from django.urls import path
from core.views import index, about, car_details, add_car

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('car_details/<int:car_pk>/', car_details, name='car_details'),
    path('add_car/', add_car, name='add_car'),
]