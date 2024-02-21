from rest_framework import serializers
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult

class UploadTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
