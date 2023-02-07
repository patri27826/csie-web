# Generated by Django 3.1.2 on 2022-07-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0041_auto_20220709_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='place',
            field=models.IntegerField(choices=[(1, '系主任'), (2, '副系主任'), (3, '講座教授'), (4, '特聘教授'), (5, '教授'), (6, '副教授'), (7, '助理教授')], default=99, verbose_name='位置'),
        ),
    ]
