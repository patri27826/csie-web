# Generated by Django 3.1.2 on 2022-04-23 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20220423_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='links',
        ),
        migrations.AddField(
            model_name='navbar',
            name='links',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.link', verbose_name='首頁連結'),
            preserve_default=False,
        ),
    ]
