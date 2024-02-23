
import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('size', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateField(blank=True, null=True)),
                ('end_time', models.DateField(blank=True, null=True)),
                ('lesson_start', models.TimeField(blank=True, null=True)),
                ('lesson_end', models.TimeField(blank=True, null=True)),
                ('student_id', models.ManyToManyField(related_name='group_student', to=settings.AUTH_USER_MODEL)),
                ('teacher_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_teacher', to=settings.AUTH_USER_MODEL)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_room', to='structure.room')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_subject', to='structure.subject')),
                ('week_id', models.ManyToManyField(blank=True, related_name='group_week', to='structure.week')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='lesson_video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mpeg', 'avi', 'flw', 'mov', 'mkv'])])),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_group', to='structure.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_student_id', to=settings.AUTH_USER_MODEL)),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_lesson_id', to='structure.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LessonSource',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='lesson_source/')),
                ('lesson_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_source_lesson_id', to='structure.lesson')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('summa', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_student_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('grade', models.IntegerField(default=0)),
                ('deadline', models.DateTimeField()),
                ('file', models.FileField(upload_to='tasks/')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_group_id', to='structure.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task_submitions',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='task_submitions/')),
                ('grade', models.IntegerField(default=0)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_submitions_student_id', to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_submitions_task_id', to='structure.tasks')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='test_file', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'xls', 'csv'])])),
                ('time', models.TimeField(blank=True, null=True)),
                ('group', models.ManyToManyField(blank=True, related_name='test_group', to='structure.group')),


                ('tester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_test', to=settings.AUTH_USER_MODEL)),


            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('question', models.TextField(blank=True, null=True)),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_question', to='structure.test')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestAnswer',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),


                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='structure.testquestion')),


            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_result', to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_result', to='structure.test')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
