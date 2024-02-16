from django.contrib import admin
from .models import (
    Group,
    Room,
    Tasks,
    Task_submitions,
    Payment,
    LessonSource,
    Lesson,
    Subject,
    Week,
    Attendance,
)
# Register your models here.

admin.site.register(Group)
admin.site.register(Room)
admin.site.register(Tasks)
admin.site.register(Task_submitions)
admin.site.register(Payment)
admin.site.register(Lesson)
admin.site.register(LessonSource)
admin.site.register(Subject)
admin.site.register(Week)
admin.site.register(Attendance)


