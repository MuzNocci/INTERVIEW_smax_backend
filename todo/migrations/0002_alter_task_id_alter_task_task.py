# Generated by Django 5.1.4 on 2025-01-02 21:02

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=50),
        ),
    ]
