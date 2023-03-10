# Generated by Django 3.1.2 on 2022-02-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_csiepicture_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/carousel', verbose_name='圖片')),
                ('content', models.TextField(blank=True, help_text='輸入內容', max_length=100, null=True, verbose_name='圖片內容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='日期')),
            ],
            options={
                'verbose_name_plural': '其他輪播圖片',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='CsiePicture',
        ),
        migrations.AlterModelOptions(
            name='carousel',
            options={'ordering': ['-date'], 'verbose_name_plural': '頁首輪播'},
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='image',
        ),
        migrations.AddField(
            model_name='carousel',
            name='csie',
            field=models.ImageField(blank=True, null=True, upload_to='images/carousel', verbose_name='系上形象圖片'),
        ),
        migrations.AddField(
            model_name='carousel',
            name='other',
            field=models.ManyToManyField(to='home.Image', verbose_name='其他圖片'),
        ),
    ]
