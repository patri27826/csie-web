# Generated by Django 3.1.2 on 2022-08-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0043_auto_20220717_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日期'),
        ),
    ]