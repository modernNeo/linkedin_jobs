# Generated by Django 4.2.3 on 2023-09-12 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_remove_job_date_posted_joblocation_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='linkedin_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='linkedin_link',
        ),
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
        migrations.RemoveField(
            model_name='job',
            name='remote_work_allowed',
        ),
    ]