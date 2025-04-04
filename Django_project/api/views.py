from django.db.models import Count
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Car, Category
from .serializers import CategorySerializer, CarListSerializer, CarDetailSerializer
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

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
    queryset = Car.objects.all().select_related('category').order_by('category_id', '-id')
    serializer_class = CarListSerializer
    pagination_class = PageNumberPagination

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all().select_related('category')
    serializer_class = CarDetailSerializer
    lookup_field = 'id'

class CarCreateView(CreateAPIView):
    serializer_class = CarDetailSerializer

class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all().select_related('category')
    serializer_class = CarDetailSerializer

class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all().select_related('category')


class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all().select_related('category').order_by('-created_at')
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CarDetailSerializer
        return CarListSerializer

class CarRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all().select_related('category')
    serializer_class = CarDetailSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all().select_related('category').order_by('-created_at')
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('create','retrieve', 'update'):
            return CarDetailSerializer
        return CarListSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=True, methods=['POST'])
    def mark_as_sold(self, request, pk=None):
        car = self.get_object()
        if car.is_sold:
            return Response("Detail: Car is already sold")
        car.is_sold = True
        car.save()
        return Response("Detail: Car marked as sold")












