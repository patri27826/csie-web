# Generated by Django 3.1.2 on 2022-02-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220211_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='輸入分頁名稱', max_length=10)),
            ],
            options={
                'verbose_name_plural': '連結',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.ManyToManyField(to='home.Link', verbose_name='首頁連結')),
            ],
            options={
                'verbose_name_plural': '首頁頂端連結',
            },
        ),
    ]
