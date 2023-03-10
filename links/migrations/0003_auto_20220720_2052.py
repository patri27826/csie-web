# Generated by Django 3.1.2 on 2022-07-20 12:52

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alumni_eecs_ncku'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumni',
            options={'verbose_name_plural': '系友資訊'},
        ),
        migrations.AlterModelOptions(
            name='eecs',
            options={'verbose_name_plural': '電資學院'},
        ),
        migrations.AlterModelOptions(
            name='ncku',
            options={'verbose_name_plural': '成功大學'},
        ),
        migrations.AlterModelOptions(
            name='other',
            options={'verbose_name_plural': '其他服務系統'},
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='content',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='date',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='image',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='link',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='title',
        ),
        migrations.RemoveField(
            model_name='eecs',
            name='content',
        ),
        migrations.RemoveField(
            model_name='eecs',
            name='date',
        ),
        migrations.RemoveField(
            model_name='eecs',
            name='image',
        ),
        migrations.RemoveField(
            model_name='eecs',
            name='link',
        ),
        migrations.RemoveField(
            model_name='eecs',
            name='title',
        ),
        migrations.RemoveField(
            model_name='ncku',
            name='content',
        ),
        migrations.RemoveField(
            model_name='ncku',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ncku',
            name='image',
        ),
        migrations.RemoveField(
            model_name='ncku',
            name='link',
        ),
        migrations.RemoveField(
            model_name='ncku',
            name='title',
        ),
        migrations.RemoveField(
            model_name='other',
            name='content',
        ),
        migrations.RemoveField(
            model_name='other',
            name='date',
        ),
        migrations.RemoveField(
            model_name='other',
            name='image',
        ),
        migrations.RemoveField(
            model_name='other',
            name='link',
        ),
        migrations.RemoveField(
            model_name='other',
            name='title',
        ),
        migrations.CreateModel(
            name='OtherTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='圖片')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='links.other')),
            ],
            options={
                'verbose_name': 'other Translation',
                'db_table': 'links_other_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='NCKUTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='圖片')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='links.ncku')),
            ],
            options={
                'verbose_name': 'ncku Translation',
                'db_table': 'links_ncku_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='EECSTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='圖片')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='links.eecs')),
            ],
            options={
                'verbose_name': 'eecs Translation',
                'db_table': 'links_eecs_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name='AlumniTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='圖片')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='links.alumni')),
            ],
            options={
                'verbose_name': 'alumni Translation',
                'db_table': 'links_alumni_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model),
        ),
    ]
