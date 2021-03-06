# Generated by Django 4.1.dev20220504101500 on 2022-05-26 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_remove_course_learner_courses_course_courselearner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='CourseLearner',
        ),
        migrations.AddField(
            model_name='course_learner',
            name='CourseLearner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.course'),
        ),
        migrations.AddField(
            model_name='course_learner',
            name='Note',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
