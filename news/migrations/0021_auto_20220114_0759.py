# Generated by Django 3.1.2 on 2022-01-14 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0020_auto_20220113_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='file2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='file3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='file4',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
    ]
