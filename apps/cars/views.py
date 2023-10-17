from .models import CarModel
from django.forms import model_to_dict
from .filters import car_filtered_queryset

from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer

class CarListCreateView(ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)

class CarsInAutopark(ListAPIView):
    # queryset = CarModel.objects.all().filter(autopark_id=1)
    serializer_class = CarSerializer
    def get_queryset(self):
        autopark_id = self.kwargs.get('pk', 1)
        print(autopark_id)
        queryset = CarModel.objects.all().filter(autopark_id=autopark_id)
        return queryset



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer