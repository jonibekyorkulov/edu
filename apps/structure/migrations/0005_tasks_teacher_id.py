# Generated by Django 5.0.2 on 2024-02-21 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0004_alter_group_week_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='teacher_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_teacher', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
