# Generated by Django 4.1.dev20220504101500 on 2022-05-22 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_instructor_created_alter_instructor_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_learner',
            old_name='teachers',
            new_name='courses',
        ),
    ]