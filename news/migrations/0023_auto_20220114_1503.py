# Generated by Django 3.1.2 on 2022-01-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_auto_20220114_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='Enter date'),
        ),
    ]
