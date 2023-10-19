from django_filters.rest_framework import DjangoFilterBackend as filters, DjangoFilterBackend

from .models import CarModel
from .filters import CarFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CarSerializer

class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)


class CarsInAutopark(ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        autopark_id = self.kwargs.get('pk', 1)
        print(autopark_id)
        queryset = CarModel.objects.all().filter(autopark_id=autopark_id)
        return queryset



class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer