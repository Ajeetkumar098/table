# Generated by Django 4.1.6 on 2023-02-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markshit_app', '0002_alter_student_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mobileno',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
