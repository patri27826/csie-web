# Generated by Django 3.1.2 on 2021-12-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_project_finish_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='finish_time',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_time',
        ),
        migrations.AddField(
            model_name='project',
            name='datethrough',
            field=models.CharField(default='', max_length=30),
        ),
    ]
