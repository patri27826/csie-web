# Generated by Django 3.1.2 on 2022-05-18 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0038_auto_20220518_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image4',
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='post/files/', verbose_name='附加檔案'),
        ),
        migrations.AlterField(
            model_name='postfile',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post'),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='post/images/', verbose_name='附加圖片')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
            options={
                'verbose_name_plural': '附加圖片',
            },
        ),
    ]