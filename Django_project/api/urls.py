from .views import (
    CategoryListView, CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    CarListCreateView, CarRetrieveUpdateDeleteView,
    CarViewSet
)
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register('cars', CarViewSet, basename='cars')

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    # path('cars/', CarListView.as_view(), name='car_list'),
    # path('cars/create/', CarCreateView.as_view(), name='car_create'),
    # path('cars/<int:id>/', CarDetailView.as_view(), name='car_details'),
    # path('cars/update/<int:pk>/', CarUpdateView.as_view(), name='car_update'),
    # path('cars/delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
    # path('cars/', CarListCreateView.as_view(), name='car_list_create'),
    # path('cars/<int:pk>/', CarRetrieveUpdateDeleteView.as_view(), name='car_detail'),
    path('', include(router.urls)),
]