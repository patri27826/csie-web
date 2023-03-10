# Generated by Django 3.1.2 on 2022-07-21 03:35

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_PhD_AdmissionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': '課程介紹',
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
        migrations.RenameModel(
            old_name='AdmissionInfo',
            new_name='Bachelor_AdmissionInfo',
        ),
        migrations.RenameModel(
            old_name='AdmissionInfoTranslation',
            new_name='Bachelor_AdmissionInfoTranslation',
        ),
        migrations.AlterModelOptions(
            name='bachelor_admissioninfotranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'bachelor_ admission info Translation'},
        ),
        migrations.AlterModelTable(
            name='bachelor_admissioninfotranslation',
            table='admission_bachelor_admissioninfo_translation',
        ),
        migrations.CreateModel(
            name='Master_PhD_AdmissionInfoTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(help_text='輸入標題', max_length=200, verbose_name='大標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('subtitle1', models.TextField(blank=True, help_text='輸入小標題', max_length=200, verbose_name='小標題一')),
                ('subcontent1', models.TextField(blank=True, help_text='輸入內容', verbose_name='小標題一內容')),
                ('subtitle2', models.TextField(blank=True, help_text='輸入小標題', max_length=200, verbose_name='小標題二')),
                ('subcontent2', models.TextField(blank=True, help_text='輸入內容', verbose_name='小標題二內容')),
                ('subtitle3', models.TextField(blank=True, help_text='輸入小標題', max_length=200, verbose_name='小標題三')),
                ('subcontent3', models.TextField(blank=True, help_text='輸入內容', verbose_name='小標題三內容')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='admission.master_phd_admissioninfo')),
            ],
            options={
                'verbose_name': 'master_ ph d_ admission info Translation',
                'db_table': 'admission_master_phd_admissioninfo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]
