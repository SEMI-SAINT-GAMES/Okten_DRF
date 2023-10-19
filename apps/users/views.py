from rest_framework.generics import ListCreateAPIView

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


