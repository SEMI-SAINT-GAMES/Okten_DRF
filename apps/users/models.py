from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from core.enums.regex_enum import RegEx
from .managers import UserManager
from core.models import BaseModel

class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'
    name = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.USER_NAME.__str__(), RegEx.USER_NAME.error_message())])
    surname = models.CharField(max_length=50, validators=[V.RegexValidator(RegEx.USER_SURNAME.__str__(), RegEx.USER_SURNAME.error_message())])
    age = models.IntegerField(null=True)

class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[V.RegexValidator(RegEx.USER_PASSWORD.__str__(), RegEx.USER_PASSWORD.error_message())])
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)


    USERNAME_FIELD = 'email'

    objects = UserManager()
