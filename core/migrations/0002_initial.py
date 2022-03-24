# Generated by Django 3.2.9 on 2021-12-14 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting_request',
            name='interviewer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting_request',
            name='student_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviewer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='interviewer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='student_t', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='interviewer_r', to=settings.AUTH_USER_MODEL),
        ),
    ]