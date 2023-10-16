from .models import (CarModel)
from django.forms import model_to_dict
from .serializers import CarSerializer
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import car_filtered_queryset

class CarListCreateView(ListCreateAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    def get_queryset(self):
        return car_filtered_queryset(self.request.query_params)

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer