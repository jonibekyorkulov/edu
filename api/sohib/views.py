from rest_framework.response import Response
from rest_framework.views import APIView
from apps.structure.permission import IsAdmin
from rest_framework.generics import ListAPIView
from .serializers import GroupGetRoomSerializer, PaymentSerializer, AttendanceSerializer
from apps.structure.models import Group, Attendance
from apps.accounts.models import User
from django.shortcuts import get_object_or_404
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def pdf_gen(user, serializer):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    c.setTitle("Shartnoma")
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    # textob.setTextTransform(1, 1, 0, 0, 0, 1)
    textob.setFont('Helvetica', 24)
    # textob.setHorizScale()
    textob.textLine("Shartnoma")
    textob.setFont('Helvetica', 14)
    textob.textLine(f"Talaba: {user.full_name}")
    textob.textLine(f"====================================")
    for obj in serializer.data:
        textob.textLines(f"\n"*2)
        textob.textLine(f"Sana: {obj['date']}")
        textob.textLine(f"Summa: {str(obj['summa'])}  so'm")
        textob.textLine(f"Izoh: {obj['comment']}")
        textob.textLines(f"\n"*2)
        textob.textLine(f"====================================")

    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return buf

class GetTable(APIView):
    permission_classes = (IsAdmin, )
    def get(self, request):
        uuid = request.data.get('uuid')
        type = request.data.get('type')
        if type == 'group':
            group = get_object_or_404(Group, uuid = uuid)
            serializer = GroupGetRoomSerializer(instance=group)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        elif type == 'teacher':
            teacher = get_object_or_404(User, uuid=uuid)
            groups = teacher.group_teacher
            print(groups)
            serializer = GroupGetRoomSerializer(instance=groups, many=True)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        elif type == 'student':
            student = get_object_or_404(User, uuid = uuid)
            groups = student.group_student
            serializer = GroupGetRoomSerializer(instance=groups, many=True)
            data = {
                'status' : True,
                'data' : serializer.data
            }
            return Response(data)
        return Response({"status":False})

class GetPayment(APIView):
    permission_classes = (IsAdmin, )
    def get(self, request):
        uuid = request.data.get('uuid')
        student = get_object_or_404(User, uuid=uuid)
        if student.role != 'student':
            return Response({'status':False})
        payments = student.payment_student_id
        serializer = PaymentSerializer(instance=payments, many=True)

        # data = {
        #     'status':True,
        #     'data' : serializer.data
        # }
        # return Response(data)
        return FileResponse(pdf_gen(student, serializer), as_attachment=True, filename="shartnoma.pdf")

class GetAttendance(ListAPIView):
    permission_classes = (IsAdmin, )
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        group = get_object_or_404(Group, uuid=self.request.data.get('uuid'))
        students = group.student_id.all()
        queryset = {}
        for student in students:
            queryset += Attendance.objects.filter(student_id = student)
        return queryset
