from .models import Car
from .serializers import CarSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CarAPIList(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer



class CarAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer