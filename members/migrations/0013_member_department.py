# Generated by Django 3.1.2 on 2021-12-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_auto_20211210_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='department',
            field=models.ManyToManyField(to='members.Department'),
        ),
    ]