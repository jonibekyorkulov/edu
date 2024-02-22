from django.shortcuts import render
from apps.structure.models import Group
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
class ClassSchedule (APIView):
    permission_classes = (AllowAny,)
    