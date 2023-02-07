# Generated by Django 4.1 on 2022-09-04 07:13

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0053_alter_office_member_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="awarded",
        ),
        migrations.RemoveField(
            model_name="member",
            name="experience",
        ),
        migrations.RemoveField(
            model_name="member",
            name="expertise",
        ),
        migrations.RemoveField(
            model_name="member",
            name="graduate",
        ),
        migrations.RemoveField(
            model_name="member",
            name="lab",
        ),
        migrations.RemoveField(
            model_name="member",
            name="lab_location",
        ),
        migrations.RemoveField(
            model_name="member",
            name="office",
        ),
        migrations.RemoveField(
            model_name="member",
            name="patent",
        ),
        migrations.RemoveField(
            model_name="member",
            name="position",
        ),
        migrations.RemoveField(
            model_name="member",
            name="project_gen",
        ),
        migrations.RemoveField(
            model_name="member",
            name="project_tech",
        ),
        migrations.RemoveField(
            model_name="member",
            name="published_accepted_papers",
        ),
        migrations.RemoveField(
            model_name="member",
            name="published_conference_domestic",
        ),
        migrations.RemoveField(
            model_name="member",
            name="published_conference_foreign",
        ),
        migrations.RemoveField(
            model_name="member",
            name="published_refered_papers",
        ),
        migrations.RemoveField(
            model_name="member",
            name="students_conference",
        ),
        migrations.RemoveField(
            model_name="member",
            name="students_doc",
        ),
        migrations.RemoveField(
            model_name="member",
            name="students_honor",
        ),
        migrations.RemoveField(
            model_name="member",
            name="students_master",
        ),
        migrations.CreateModel(
            name="MemberTranslation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                (
                    "expertise",
                    models.TextField(
                        default="", help_text="專長及研究領域", verbose_name="專長及研究領域"
                    ),
                ),
                (
                    "graduate",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="學歷（國家 \\ 學校 \\ 系別 \\ 學歷(修業期間)）eg. 美國 \\ 華盛頓州立大學 \\ 資訊工程 \\ 博士(1992 ~ 1995)",
                        verbose_name="學歷",
                    ),
                ),
                (
                    "experience",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="經歷（經歷(時間)）",
                        verbose_name="經歷",
                    ),
                ),
                (
                    "patent",
                    models.TextField(
                        blank=True, default="", help_text="專利號 專利名稱", verbose_name="專利"
                    ),
                ),
                (
                    "awarded",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="榮譽及獲獎（(時間)獲獎名稱）",
                        verbose_name="榮譽及獲獎",
                    ),
                ),
                (
                    "published_accepted_papers",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="著作——Accepted Papers to be Published",
                        verbose_name="著作——Accepted Papers to be Published",
                    ),
                ),
                (
                    "published_refered_papers",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="著作——Refereed Papers",
                        verbose_name="著作——Refereed Papers",
                    ),
                ),
                (
                    "published_conference_foreign",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="著作——Conference Papers（國際會議）",
                        verbose_name="著作——Conference Papers（國際會議）",
                    ),
                ),
                (
                    "published_conference_domestic",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="著作——Conference Papers（國內會議）",
                        verbose_name="著作——Conference Papers（國內會議）",
                    ),
                ),
                (
                    "project_tech",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="科技部計劃（計劃名稱 / 起迄日期 / 補助單位）",
                        verbose_name="科技部計劃",
                    ),
                ),
                (
                    "project_gen",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="一般建教案（計劃名稱 / 起迄日期 / 補助單位）",
                        verbose_name="一般建教案",
                    ),
                ),
                (
                    "students_doc",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="博士生（姓名(年級)）",
                        verbose_name="博士生",
                    ),
                ),
                (
                    "students_master",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="碩士生（姓名(年級)）",
                        verbose_name="碩士生",
                    ),
                ),
                (
                    "students_honor",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="指導學生之特殊榮譽（時間 / 得獎名稱）",
                        verbose_name="指導學生之特殊榮譽",
                    ),
                ),
                (
                    "students_conference",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="主辦及參與國際會議（時間 / 會議名稱）",
                        verbose_name="主辦及參與國際會議",
                    ),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="members.member",
                    ),
                ),
            ],
            options={
                "verbose_name": "member Translation",
                "db_table": "members_member_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]