from rest_framework import serializers
from apps.structure.models import Test, TestQuestion, TestAnswer, TestResult
from rest_framework.exceptions import ValidationError
from apps.accounts.models import User

class UploadTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

    def validate(self, data):
        file = data.get('file', None)
        if not file:
            data = {
                'message' : 'Has not file'
            }
            raise ValidationError(data)
        
        tester = data.get('tester', None)
        if not tester:
            data = {
                'status' : False,
                'message' : "Has not tester"
            }
            raise ValidationError(data)
        return data
        

class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"
        

    