# Generated by Django 3.1.2 on 2022-03-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homeinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinfo',
            name='content',
            field=models.TextField(help_text='輸入內容', max_length=200, verbose_name='內容'),
        ),
    ]
