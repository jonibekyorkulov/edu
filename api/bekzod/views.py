from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
from api.bekzod.serializers import AttendanceSerializers, Attendance


class AttendanceRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = AttendanceSerializers
    permission_classes  = [IsAdminUser,]

    def get_queryset(self):
        return Attendance.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        sz = self.get_serializer(instance)
        return Response(sz.data, status=status.HTTP_200_OK)
    
