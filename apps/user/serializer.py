from rest_framework import serializers
from apps.user.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'name', 'auto_parks',)
        read_only_fields = ('auto_parks',)
