# Generated by Django 3.1.2 on 2021-12-10 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20211210_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_name',
            name='grade',
            field=models.CharField(choices=[('1', '碩一'), ('2', '碩二'), ('3', '博一'), ('4', '博二'), ('5', '博三'), ('6', '博四'), ('7', '博五'), ('8', '博六'), ('9', '博七')], max_length=1),
        ),
    ]
