# Generated by Django 3.1.2 on 2022-02-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='圖片')),
                ('content', models.TextField(blank=True, help_text='輸入內容', max_length=100, null=True, verbose_name='圖片內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='公告日期')),
            ],
            options={
                'verbose_name_plural': '輪播圖片',
                'ordering': ['-date'],
            },
        ),
    ]
