# Generated by Django 4.1.1 on 2022-09-16 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0046_alter_externallink_options_alter_homeimage_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={"ordering": ["-date"], "verbose_name_plural": "輪播圖片上傳"},
        ),
    ]