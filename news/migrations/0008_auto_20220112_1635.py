# Generated by Django 3.1.2 on 2022-01-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20220112_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ManyToManyField(blank=True, to='news.File'),
        ),
    ]
