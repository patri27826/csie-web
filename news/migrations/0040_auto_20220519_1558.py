# Generated by Django 3.1.2 on 2022-05-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20220519_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='公告日期'),
        ),
    ]