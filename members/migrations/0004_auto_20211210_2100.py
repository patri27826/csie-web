# Generated by Django 3.1.2 on 2021-12-10 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_project_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
