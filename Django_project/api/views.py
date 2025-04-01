from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from core.models import Car, Category
from .serializers import CategorySerializer, CarSerializer, CarDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# @api_view()
# def category_list(request):
#     categories = Category.objects.all().annotate(car_count=Count('cars'))
#     serializer = CategorySerializer(categories, many=True)
#     return Response(serializer.data)
#
# @api_view()
# def car_list(request):
#     cars = Car.objects.all()
#     serializer = CarSerializer(cars, many=True, context={'request': request})
#     return Response(serializer.data)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all().annotate(car_count=Count('cars'))
    serializer_class = CategorySerializer

class CarListView(ListAPIView):
    queryset = Car.objects.all().select_related('category')
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all().select_related('category')
    serializer_class = CarDetailSerializer
    lookup_field = 'id'













