# Generated by Django 3.1.2 on 2022-04-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='title',
            field=models.CharField(help_text='輸入標題', max_length=200, verbose_name='標題'),
        ),
    ]
