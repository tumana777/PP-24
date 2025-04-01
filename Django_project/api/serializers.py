from rest_framework import serializers
from core.models import Car, Category

# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     category_name = serializers.CharField(source='name')
#     car_count = serializers.IntegerField(required=False)
#
# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     make = serializers.CharField()
#     model = serializers.CharField()
#     description = serializers.CharField()
#     year = serializers.IntegerField()
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     # category = serializers.CharField()
#     is_sold = serializers.BooleanField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     quantity = serializers.IntegerField()
#     image = serializers.ImageField()
#     category = CategorySerializer()
#     total = serializers.SerializerMethodField(method_name='get_total_price')
#
#     def get_total_price(self, obj):
#         return obj.price * obj.quantity

class CategorySerializer(serializers.ModelSerializer):

    car_count = serializers.CharField(required=False)

    class Meta:
        model = Category
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):

    category = CategorySerializer()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'category')

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'