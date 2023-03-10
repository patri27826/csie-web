# Generated by Django 3.1.2 on 2022-07-25 07:06

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20220721_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeimage',
            name='image',
        ),
        migrations.CreateModel(
            name='homeImageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('image', models.ImageField(upload_to='images/', verbose_name='圖片')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='home.homeimage')),
            ],
            options={
                'verbose_name': 'home image Translation',
                'db_table': 'home_homeimage_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases = (parler.models.TranslatableModel, models.Model)
        ),
    ]
