# Generated by Django 3.1.2 on 2022-02-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220216_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(choices=[('本系簡介', '本系簡介'), ('師資陣容', '師資陣容'), ('系所公告', '系所公告'), ('招生資訊', '招生資訊')], default='系所公告', max_length=20),
        ),
    ]