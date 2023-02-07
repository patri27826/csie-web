# Generated by Django 3.1.2 on 2022-03-02 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220216_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='圖片')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
            ],
            options={
                'verbose_name_plural': '資訊要聞',
                'ordering': ['-date'],
            },
        ),
    ]
