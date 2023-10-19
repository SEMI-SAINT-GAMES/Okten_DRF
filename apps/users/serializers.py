from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import ProfileModel

UserModel = get_user_model()

class ProfileSerializer(serializers.Serializer):

    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'created_at', 'updated_at')
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at', 'profile'
        )
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'is_active', 'last_login', 'created_at', 'updated_at' )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        return user

