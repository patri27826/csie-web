# Generated by Django 3.1.2 on 2022-08-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0006_auto_20220805_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centerstranslation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
        ),
        migrations.AlterField(
            model_name='internationaltranslation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
        ),
    ]
