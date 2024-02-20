from rest_framework import serializers
from apps.structure.models import Group


class GroupGetRoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name', 'subject_id', 'week_id', 'lesson_start', 'lesson_end')