# Generated by Django 3.1.2 on 2022-05-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_auto_20220423_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navbar',
            options={'verbose_name_plural': '首頁快速連結'},
        ),
        migrations.AlterField(
            model_name='navbar',
            name='links',
            field=models.CharField(choices=[('系所公告', '系所公告'), ('系所介紹', '系所介紹'), ('榮譽事蹟', '榮譽事蹟'), ('法規彙編', '法規彙編'), ('交通資訊', '交通資訊'), ('場地租借', '場地租借'), ('課程介紹', '課程介紹'), ('大學部', '大學部'), ('碩博士', '碩博士'), ('產業碩士專班', '產業碩士專班'), ('畢業生', '畢業生'), ('文件下載', '文件下載'), ('國際合作交流', '國際合作交流'), ('大學部招生', '大學部招生'), ('碩士招生', '碩士招生'), ('博士招生', '博士招生'), ('師資陣容', '師資陣容'), ('系辦成員', '系辦成員'), ('實驗室', '實驗室'), ('研究群', '研究群'), ('研究中心', '研究中心'), ('其他服務系統', '其他服務系統'), ('成功大學', '成功大學'), ('電資學院', '電資學院'), ('系友資訊', '系友資訊')], max_length=20, verbose_name='首頁快速連結'),
        ),
    ]