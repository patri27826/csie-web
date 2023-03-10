# Generated by Django 3.1.2 on 2022-04-08 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_auto_20220408_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venue',
            options={'ordering': ['date'], 'verbose_name_plural': '場地租借'},
        ),
        migrations.AddField(
            model_name='venue',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
