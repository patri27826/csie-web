# Generated by Django 3.1.2 on 2022-01-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20220112_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='post',
            name='file4',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.DeleteModel(
            name='PostFile',
        ),
    ]
