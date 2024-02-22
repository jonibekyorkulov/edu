from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from apps.accounts.models import User


class TeacherProfilGetSerializers(serializers.ModelSerializer):
    password = serializers.CharField(required = False)
    username = serializers.CharField(required = False)
    class Meta:
        model = User
        fields = "__all__"


    # def validate(self, data):
    #     attrs =  super().validate(data)


# class TeacherProfilUpdateSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ('phone_namber', 'address', 'region', 'district', 'photo','tg_username')



# class TeacherProfilGetSerializers(serializers):
    # role = serializers.CharField(max_length=255, null=True, blank=True)
    # first_name = serializers.CharField(max_length=255, null=True, blank=True)
    # last_name = serializers.CharField(max_length=255, null=True, blank=True)
    # middle_name = serializers.CharField(max_length=255, null=True, blank=True)
    # phone_namber = serializers.CharField(max_length=255, null=True, blank=True)
    # passport = serializers.CharField(max_length=255, null=True, blank=True)
    # jshir = serializers.BigIntegerField(null=True, blank=True)
    # gender = serializers.CharField(max_length=255, null=True, blank=True)
    # address = serializers.CharField(max_length=255, null=True, blank=True)
    # region = serializers.CharField(max_length=255, null=True, blank=True)
    # district = serializers.CharField(max_length=255, null=True, blank=True)
    # photo = serializers.ImageField(upload_to='user/', null=True, blank=True, validators=[
    #     FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'heic', 'heif'])
    # ])
    # birthday = serializers.DateField(null = True, blank = True)
    # tg_username = serializers.CharField(max_length = 255)