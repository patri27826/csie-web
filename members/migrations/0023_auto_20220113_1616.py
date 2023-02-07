# Generated by Django 3.1.2 on 2022-01-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_remove_patent_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patent',
            name='professor_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='professor_name',
        ),
        migrations.RemoveField(
            model_name='published',
            name='professor_name',
        ),
        migrations.RemoveField(
            model_name='student_conference',
            name='professor_name',
        ),
        migrations.RemoveField(
            model_name='student_honor',
            name='professor_name',
        ),
        migrations.RemoveField(
            model_name='student_name',
            name='professor_name',
        ),
        migrations.AddField(
            model_name='member',
            name='patent',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='member',
            name='published_accepted_papers',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='member',
            name='published_conference_papers',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='member',
            name='published_refered_papers',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='email1',
            field=models.EmailField(default='', help_text='E-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='email2',
            field=models.EmailField(blank=True, default='', help_text='E-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='email3',
            field=models.EmailField(blank=True, default='', help_text='E-mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='member',
            name='expertise',
            field=models.TextField(default='', help_text='專長及研究領域'),
        ),
        migrations.AlterField(
            model_name='member',
            name='graduate',
            field=models.TextField(default='', help_text='學歷（國家 \\ 學校 \\ 系別 \\ 學歷（修業期間））'),
        ),
        migrations.AlterField(
            model_name='member',
            name='lab',
            field=models.CharField(default='', help_text='實驗室名稱', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='lab_location',
            field=models.CharField(default='', help_text='實驗室位置', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(help_text='姓名', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='office',
            field=models.CharField(default='資訊系館', help_text='辦公室位置', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(default='', help_text='電話，分機', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(default='', help_text='職位', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='website',
            field=models.CharField(blank=True, default='', help_text='個人網頁', max_length=100),
        ),
        migrations.DeleteModel(
            name='Honor',
        ),
        migrations.DeleteModel(
            name='Patent',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Published',
        ),
        migrations.DeleteModel(
            name='Student_Conference',
        ),
        migrations.DeleteModel(
            name='Student_Honor',
        ),
        migrations.DeleteModel(
            name='Student_Name',
        ),
    ]