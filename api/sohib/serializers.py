from rest_framework import serializers


class GroupGetRoomSerializer(serializers.Serializer):
    group_id = serializers.UUIDField(required = True)
    room_id = serializers.UUIDField(required = True)
    start_time = serializers.TimeField(required = True)
    end_time = serializers.TimeField(required = True)