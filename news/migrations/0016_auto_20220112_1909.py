# Generated by Django 3.1.2 on 2022-01-12 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20220112_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='files',
        ),
        migrations.DeleteModel(
            name='Files',
        ),
        migrations.AddField(
            model_name='postfile',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='news.post'),
        ),
    ]
