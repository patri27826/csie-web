# Generated by Django 3.1.2 on 2022-07-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0042_auto_20220519_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='輸入內容', verbose_name='公告內容'),
        ),
    ]
