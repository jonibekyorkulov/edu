# Generated by Django 5.0.2 on 2024-02-22 16:25

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('is_active', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='user_file/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['xlsx', 'xls', 'csv'])])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
