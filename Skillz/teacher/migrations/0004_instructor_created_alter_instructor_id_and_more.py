# Generated by Django 4.1.dev20220504101500 on 2022-05-22 14:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0003_remove_instructor_teachers_instructor_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 22, 14, 9, 31, 976698, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Course_Learner',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teachers', models.ManyToManyField(to='teacher.course')),
            ],
        ),
    ]