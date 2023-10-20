from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

class GetUsersView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        me = self.request.user
        queryset = UserModel.objects.exclude(id=me.id)
        return queryset


