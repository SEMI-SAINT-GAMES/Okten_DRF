from django.shortcuts import render
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView,  RetrieveUpdateDestroyAPIView
from apps.autoparks.models import AutoParkModel
from apps.autoparks.serializre import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from rest_framework.pagination import PageNumberPagination


class AutoparkListCreateView(ListAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    pagination_class = PageNumberPagination



class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()
    def post(self, *args, **kwargs):
        autopark = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autopark=autopark)
        park_serializer = AutoParkSerializer(autopark)

        return Response(park_serializer.data, status.HTTP_200_OK)
class AutoParkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer






