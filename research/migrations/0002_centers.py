# Generated by Django 3.1.2 on 2022-04-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='輸入標題', max_length=200, verbose_name='標題')),
                ('content', models.TextField(blank=True, help_text='輸入內容', max_length=1000, verbose_name='內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='圖片')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='相關連結')),
            ],
            options={
                'verbose_name_plural': '研究中心',
                'ordering': ['date'],
            },
        ),
    ]
