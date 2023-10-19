from rest_framework.generics import CreateAPIView, ListAPIView

from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class GetUsersView(ListAPIView):
    pass


