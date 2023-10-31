from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from core.permissions import IsCustomer, IsStaff
from .models import PartRequestModel
from .serializers import PartRequestSerializer
from rest_framework.pagination import PageNumberPagination


class ListCreatePartRequestView(ListCreateAPIView):
     queryset = PartRequestModel.objects.all()
     permission_classes = (IsStaff,)
     serializer_class = PartRequestSerializer
     pagination_class = PageNumberPagination

class DestroyParRequestView(DestroyAPIView):
     permission_classes = (AllowAny,)
     queryset = PartRequestModel.objects.all()
     serializer_class = PartRequestSerializer



