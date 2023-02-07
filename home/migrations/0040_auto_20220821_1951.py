# Generated by Django 3.1.2 on 2022-08-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20220821_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='連結網址'),
        ),
        migrations.AlterField(
            model_name='link',
            name='text',
            field=models.URLField(blank=True, null=True, verbose_name='顯示文字'),
        ),
    ]
