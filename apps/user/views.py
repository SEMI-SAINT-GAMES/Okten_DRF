from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from apps.autoparks.serializre import AutoParkSerializer
from apps.user.models import UserModel
from apps.user.serializer import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

class UserAddAutoparkView(GenericAPIView):
    queryset = UserModel.objects.all()
    def post(self, *args, **kwargs):
         users = self.get_object()
         data = self.request.data
         serializer = AutoParkSerializer(data=data)
         serializer.is_valid(raise_exception=True)
         serializer.save(users=users)
         users_serializer = UserSerializer(users)
         return Response(users_serializer.data, status.HTTP_200_OK)

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer