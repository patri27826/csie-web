# Generated by Django 3.1.2 on 2022-08-05 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0005_auto_20220805_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='centerstranslation',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='圖片'),
        ),
        migrations.AddField(
            model_name='internationaltranslation',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='圖片'),
        ),
    ]