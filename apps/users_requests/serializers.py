from rest_framework import serializers
from .models import PartRequestModel
class PartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequestModel
        fields = ('id', 'car_brand', 'car_model', 'part_name', 'vin', 'oem', 'about', 'engine_volume')