# Generated by Django 3.1.2 on 2022-07-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20220719_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinfotranslation',
            name='content',
            field=models.TextField(help_text='輸入內容', verbose_name='內容'),
        ),
    ]
