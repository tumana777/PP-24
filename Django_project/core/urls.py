
from django.urls import path
from core.views import index, about, car_details, add_car, update_car

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('car_details/<int:car_pk>/', car_details, name='car_details'),
    path('add_car/', add_car, name='add_car'),
    path('update_car/<int:car_pk>/', update_car, name='update_car'),
]