from django.db import models
from core.enums.regex_enum import RegEx
from core.models import BaseModel
from django.core import validators as V

#from core.services.upload_avatar import upload_avatar_for_cars


class PartRequestModel(BaseModel):
    class Meta:
        db_table = 'part_requests'
    car_brand = models.CharField(max_length=30, validators=[V.RegexValidator(RegEx.BRAND.__str__(), RegEx.BRAND.error_message())])
    car_model = models.CharField(max_length=30) #validators=[V.RegexValidator(RegEx.BRAND.__str__(), RegEx.BRAND.error_message())])
    part_name = models.CharField(max_length=30, validators=[V.RegexValidator(RegEx.BRAND.__str__(), RegEx.BRAND.error_message())])
    vin = models.CharField(max_length=20)# validators=[V.RegexValidator(RegEx.VIN.__str__(), RegEx.VIN.error_message())])
    oem = models.CharField(max_length=40) #[V.RegexValidator(RegEx.VIN.__str__(), RegEx.VIN.error_message())])
    about = models.CharField(max_length=10000)
    engine_volume = models.FloatField(validators=[V.MinValueValidator(0.2), V.MaxValueValidator(10.0)])

    #avatar = models.ImageField(upload_to=upload_avatar_for_cars, blank=True)
