# Generated by Django 3.1.2 on 2022-07-09 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0042_auto_20220709_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['place', 'name'], 'verbose_name_plural': '師資成員'},
        ),
    ]
