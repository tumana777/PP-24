from .views import CategoryListView, CarListView, CarDetailView
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:id>/', CarDetailView.as_view(), name='car_details'),
]