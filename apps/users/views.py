from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer



class GetUsersView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        me = self.request.user
        serializer = UserSerializer(me)
        my_email = serializer.data['email']
        print('data')
        print(serializer.data['email'])
        print('me')
        print(users)
        return Response({"lll": "kkk"})


