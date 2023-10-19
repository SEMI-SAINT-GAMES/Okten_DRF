from django.db import models
from core.models import BaseModel
from apps.user.models import UserModel
from core.enums.regex_enum import RegEx
from django.core import validators as V
class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'
    name = models.CharField(max_length=30, validators=[V.RegexValidator(RegEx.AUTO_PARK.__str__(), RegEx.AUTO_PARK.error_message())])
    users = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')