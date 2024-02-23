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
    Test,
    TestQuestion,
    TestAnswer,
    TestResult
)
# Register your models here.

admin.site.register(Group)
admin.site.register(Room)
admin.site.register(Tasks)
class TaskSubmitionsAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'student_id', "grade"]
    readonly_fields = ["grade"]

admin.site.register(Task_submitions, TaskSubmitionsAdmin)
admin.site.register(Payment)
admin.site.register(Lesson)
admin.site.register(LessonSource)
admin.site.register(Subject)
admin.site.register(Week)
admin.site.register(Attendance)


class TestAdmin(admin.ModelAdmin):
    list_display = ['tester', 'create_date']
admin.site.register(Test, TestAdmin)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(TestResult)


