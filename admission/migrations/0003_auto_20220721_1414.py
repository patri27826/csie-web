# Generated by Django 3.1.2 on 2022-07-21 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_auto_20220721_1135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bachelor_admissioninfo',
            options={'verbose_name_plural': '大學部招生'},
        ),
        migrations.AlterModelOptions(
            name='master_phd_admissioninfo',
            options={'verbose_name_plural': '研究所招生'},
        ),
    ]
