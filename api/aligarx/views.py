from .serializers import TeacherProfilGetSerializers
from rest_framework.views import APIView
from rest_framework import generics
from apps.accounts.models import User
from apps.structure.permission import IsTeacher
from .serializers import TeacherProfilGetSerializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import uuid
from django.shortcuts import get_object_or_404



class TeacherApiViewList(APIView):
    serializer_class = TeacherProfilGetSerializers
    permission_classes = (IsTeacher, )

    def get(self, request, uuid):
        object = get_object_or_404(User, uuid=uuid)
        serializers = self.serializer_class(instance = object)
        data = {
            "status" : True,
            "data" : serializers.data
        }
        return Response(data)
    
    def put(self, request, uuid):
        object = get_object_or_404(User, uuid = uuid)
        serializers = self.serializer_class(instance=object, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user = request.user)
            print(request.user)
            data = {
                "status" : True,
                "data" : serializers.data
            }
            return Response(data)



# class TeacherApiViewUpdate(generics.UpdateAPIView):
#     permission_classes = IsTeacher
#     queryset = User.objects.all()
#     serializer_class = TeacherProfilUpdateSerializers

        


