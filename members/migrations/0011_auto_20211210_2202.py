# Generated by Django 3.1.2 on 2021-12-10 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20211210_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='Email1',
            new_name='email1',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='Email2',
            new_name='email2',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='Email3',
            new_name='email3',
        ),
        migrations.RenameField(
            model_name='office_member',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='office_member',
            old_name='Resbonsibility',
            new_name='resbonsibility',
        ),
    ]
