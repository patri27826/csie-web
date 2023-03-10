# Generated by Django 3.1.2 on 2022-01-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20220112_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='', help_text='Enter filename', max_length=20)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
        migrations.DeleteModel(
            name='PostFile',
        ),
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.ManyToManyField(blank=True, to='news.Files'),
        ),
    ]
