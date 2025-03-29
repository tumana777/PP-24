from rest_framework.permissions import IsAuthenticated
from core.models import Car
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

@api_view()
@permission_classes([IsAuthenticated])
def car_list(request):
    cars = Car.objects.values().order_by('-created_at')
    return Response({'cars': cars})