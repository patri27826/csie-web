# Generated by Django 3.1.2 on 2022-07-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0039_auto_20220709_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='place',
            field=models.IntegerField(choices=[(1, 'Chair'), (2, 'Vice Chair'), (3, 'Chair Prof'), (4, 'Distinguished Prof'), (5, 'Prof'), (6, 'Associate Prof'), (7, 'Assistant Prof')], default=99),
        ),
    ]
