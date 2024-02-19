from django.db import models
from apps.base.models import BaseModel, RegionModel
from apps.base.enum import UserRol, Gender
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class User(BaseModel, AbstractUser):
    role=models.CharField(null=True, blank=True, choices=UserRol.choices())
    first_name=models.CharField(max_length=255, null=True, blank=True)
    last_name=models.CharField(max_length=255, null=True, blank=True)
    middle_name=models.CharField(max_length=255, null=True, blank=True)
    phone_namber=models.CharField(max_length=255, null=True, blank=True)
    passport = models.CharField(max_length=255, null=True, blank=True)
    jshir = models.BigIntegerField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=Gender.choices())
    address = models.CharField(null=True, blank=True)
    region = models.ForeignKey(RegionModel, on_delete = models.SET_NULL, null=True, blank=True, related_name = 'user_region')
    district = models.ForeignKey(RegionModel, on_delete = models.SET_NULL, null=True, blank=True, related_name = 'user_district')
    photo= models.ImageField(upload_to='user/', null=True, blank=True, validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    ])

    birthday = models.DateField(null = True, blank = True)
    tg_username = models.CharField(max_length = 255)


    @property
    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.last_name} {self.middle_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)

        data = {
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }

        return data

        

    def save(self, *args,**kwargs):

        if not self.password:
            self.password = self.passport
            self.set_password(self.password)
        
        if not self.username:
            self.username = self.passport

        super(User, self).save(*args,**kwargs)



    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
