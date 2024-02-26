from .serializers import TeacherProfilGetSerializers
from rest_framework.views import APIView
from rest_framework import generics
from apps.accounts.models import User
from apps.structure.permission import IsTeacher
from .serializers import TeacherProfilGetSerializers, TeacherProfilUpdateSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import uuid


class TeacherProfileList(APIView):
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

# class TeacherProfileList(generics.ListAPIViewAPIView):
#     queryset = User.objects.all()
#     serializer_class = TeacherProfilGetSerializers
#     permission_classes = (IsTeacher, )



class TeacherProfileUpdate(APIView):

    serializer_class = TeacherProfilUpdateSerializers
    permission_classes = (IsTeacher, )

    def put(self,request):
        teacher = request.user
        serializer = self.serializer_class(instance=teacher, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status" : True,
                "data" : serializer.data

            }
            return Response(data)

    
    # def put(self, request, uuid):
    #     object = get_object_or_404(User, uuid = uuid)
    #     serializers = self.serializer_class(instance=object, data=request.data)
    #     if serializers.is_valid(raise_exception=True):
    #         serializers.save(user = request.user)
    #         print(request.user)
    #         data = {
    #             "status" : True,
    #             "data" : serializers.data
    #         }
    #         return Response(data)
    


# class TeacherApiViewList(generics.UpdateAPIView):
#     permission_classes = IsTeacher
#     queryset = User.objects.all()
#     serializer_class = TeacherProfilGetSerializers

        


