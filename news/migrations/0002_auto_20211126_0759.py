# Generated by Django 3.1.2 on 2021-11-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Enter content', max_length=1000),
        ),
    ]
