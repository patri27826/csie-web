# Generated by Django 3.1.2 on 2022-08-05 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_auto_20220721_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subcontent1',
        ),
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subcontent2',
        ),
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subcontent3',
        ),
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subtitle1',
        ),
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subtitle2',
        ),
        migrations.RemoveField(
            model_name='bachelor_admissioninfotranslation',
            name='subtitle3',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subcontent1',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subcontent2',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subcontent3',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subtitle1',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subtitle2',
        ),
        migrations.RemoveField(
            model_name='master_phd_admissioninfotranslation',
            name='subtitle3',
        ),
        migrations.AddField(
            model_name='bachelor_admissioninfotranslation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master_phd_admissioninfotranslation',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bachelor_admissioninfotranslation',
            name='title',
            field=models.CharField(blank=True, help_text='????????????', max_length=200, verbose_name='??????'),
        ),
        migrations.AlterField(
            model_name='master_phd_admissioninfotranslation',
            name='title',
            field=models.CharField(blank=True, help_text='????????????', max_length=200, verbose_name='??????'),
        ),
    ]
