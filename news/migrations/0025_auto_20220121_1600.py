# Generated by Django 3.1.2 on 2022-01-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, help_text='相關連結', null=True),
        ),
    ]
