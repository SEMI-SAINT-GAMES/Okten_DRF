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
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer