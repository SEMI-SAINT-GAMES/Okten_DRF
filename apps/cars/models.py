from django.db import models
from core.models import BaseModel
from apps.autoparks.models import AutoParkModel
class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=30)
    price = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_volume = models.FloatField()
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

