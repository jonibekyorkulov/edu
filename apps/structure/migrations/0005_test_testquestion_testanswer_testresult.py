# Generated by Django 5.0.2 on 2024-02-20 16:25

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_alter_group_week_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_nswer', to='structure.testquestion')),
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
