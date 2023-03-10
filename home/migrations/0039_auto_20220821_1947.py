# Generated by Django 3.1.2 on 2022-08-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20220725_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, help_text='輸入連結網址', null=True, verbose_name='顯示文字')),
                ('text', models.CharField(blank=True, max_length=50, null=True, verbose_name='連結網址')),
            ],
            options={
                'verbose_name_plural': '首頁快速連結',
            },
        ),
        migrations.DeleteModel(
            name='Navbar',
        ),
        migrations.AlterField(
            model_name='externallink',
            name='description',
            field=models.TextField(blank=True, help_text='輸入內容', null=True, verbose_name='圖片描述'),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='link',
            field=models.URLField(help_text='輸入連結網址', verbose_name='相關連結'),
        ),
    ]
