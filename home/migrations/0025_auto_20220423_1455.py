# Generated by Django 3.1.2 on 2022-04-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20220423_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='links',
        ),
        migrations.AddField(
            model_name='navbar',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
