# Generated by Django 3.1.2 on 2022-01-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0023_auto_20220114_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, help_text='相關連結', max_length=200, null=True),
        ),
    ]