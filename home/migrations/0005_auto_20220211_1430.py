# Generated by Django 3.1.2 on 2022-02-11 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220211_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='content',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, help_text='輸入內容', max_length=100, null=True, verbose_name='圖片描述'),
        ),
    ]