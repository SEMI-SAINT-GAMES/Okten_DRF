from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from .models import PartRequestModel
from .serializers import PartRequestSerializer


class ListCreatePartRequestView(ListCreateAPIView):
     queryset = PartRequestModel.objects.all()
     permission_classes = (AllowAny,)
     serializer_class = PartRequestSerializer

