# Generated by Django 5.0.2 on 2024-02-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
