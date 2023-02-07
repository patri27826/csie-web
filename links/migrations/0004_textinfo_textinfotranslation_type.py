# Generated by Django 3.1.2 on 2022-08-14 08:41

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20220720_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a post type', max_length=20)),
            ],
            options={
                'verbose_name_plural': '資訊類型',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TextInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ManyToManyField(to='links.Type', verbose_name='類型')),
            ],
            options={
                'verbose_name_plural': '文字資訊',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TextInfoTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', verbose_name='內容')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='links.textinfo')),
            ],
            options={
                'verbose_name': 'text info Translation',
                'db_table': 'links_textinfo_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
