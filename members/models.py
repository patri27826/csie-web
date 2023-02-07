from django.db import models
from django.db.models.deletion import RESTRICT, SET_NULL
from django.urls import reverse
from datetime import date
from multiselectfield import MultiSelectField
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

##########################師資陣容##########################
# 系所
class Department(models.Model):
    name = models.CharField(max_length=10, help_text='輸入系所名稱', verbose_name='系所別')
    edit_time = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = '系所'

    def __str__(self):
        return self.name

class Classification(models.Model):
    name = models.CharField(max_length=10, help_text='輸入類別', verbose_name='類別')
    edit_time = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = '類別'

    def __str__(self):
        return self.name

class Member(TranslatableModel):
    
    PLACE_CHOICES = [
        (99, '其他'),
        (1, '系主任'),
        (2, '副系主任'),
        (3, '講座教授'),
        (4, '特聘教授'),
        (5, '教授'),
        (6, '副教授'),
        (7, '助理教授'),
    ] 

    name = models.CharField(max_length=100, default='', help_text='輸入姓名', verbose_name='姓名')
    name_en = models.CharField(max_length=100, default='', help_text='輸入英文姓名', verbose_name='英文姓名')
    
    department = models.ManyToManyField(Department, verbose_name='系所別')
    classification = models.ManyToManyField(Classification, verbose_name='類別')
    place = models.IntegerField(choices=PLACE_CHOICES, default=99, verbose_name='位置')
    order = models.IntegerField(default=99, verbose_name='排序')
    
    email1 = models.EmailField(blank=False, default='', help_text='E-mail', verbose_name='E-mail')
    email2 = models.EmailField(blank=True, default='', help_text='E-mail', verbose_name='E-mail')
    email3 = models.EmailField(blank=True, default='', help_text='E-mail', verbose_name='E-mail')
    phone = models.CharField(max_length=50, default='', help_text='電話，分機', verbose_name='電話，分機')
    photo = models.ImageField(upload_to='images/member/teacher', blank=True, null=True, verbose_name='照片')
    
    lab_website = models.CharField(max_length=200, blank=True, default='', help_text='實驗室網頁', verbose_name='實驗室網頁')
    website = models.CharField(max_length=200, blank=True, default='', help_text='個人網頁', verbose_name='個人網頁')
    translations = TranslatedFields(
        position = models.CharField(max_length=100, default='', help_text='輸入職位', verbose_name='職位'),
        office = models.CharField(max_length=200, blank=True, default='資訊系館', help_text='辦公室位置', verbose_name='辦公室位置'),
        lab = models.CharField(max_length=100, blank=True, default='', help_text='實驗室名稱', verbose_name='實驗室名稱'),
        lab_location = models.CharField(max_length=100, blank=True,default='', help_text='實驗室位置', verbose_name='實驗室位置'),
        expertise = models.TextField(default='', help_text='專長及研究領域', verbose_name='專長及研究領域'),
        graduate = models.TextField(default='', blank=True, help_text='學歷（國家 \ 學校 \ 系別 \ 學歷(修業期間)）eg. 美國 \ 華盛頓州立大學 \ 資訊工程 \ 博士(1992 ~ 1995)', verbose_name='學歷'),
        experience = models.TextField(blank=True, default='', help_text='經歷（經歷(時間)）', verbose_name='經歷'),
        patent = models.TextField(blank=True, default='', help_text='專利號 專利名稱', verbose_name='專利'),
        awarded = models.TextField(blank=True, default='', help_text='榮譽及獲獎（(時間)獲獎名稱）', verbose_name='榮譽及獲獎'),
        published_accepted_papers = models.TextField(blank=True, default='', help_text='著作——Accepted Papers to be Published', verbose_name='著作——Accepted Papers to be Published'),
        published_refered_papers = models.TextField(blank=True, default='', help_text='著作——Refereed Papers', verbose_name='著作——Refereed Papers'),
        published_conference_foreign = models.TextField(blank=True, default='', help_text='著作——Conference Papers（國際會議）', verbose_name='著作——Conference Papers（國際會議）'),
        published_conference_domestic = models.TextField(blank=True, default='', help_text='著作——Conference Papers（國內會議）', verbose_name='著作——Conference Papers（國內會議）'),
        project_tech = models.TextField(blank=True, default='', help_text='科技部計劃（計劃名稱 / 起迄日期 / 補助單位）', verbose_name='科技部計劃'),
        project_gen = models.TextField(blank=True, default='', help_text='一般建教案（計劃名稱 / 起迄日期 / 補助單位）', verbose_name='一般建教案'),
        students_doc = models.TextField(blank=True, default='', help_text='博士生（姓名(年級)）', verbose_name='博士生'),
        students_master = models.TextField(blank=True, default='', help_text='碩士生（姓名(年級)）', verbose_name='碩士生'),
        students_honor = models.TextField(blank=True, default='', help_text='指導學生之特殊榮譽（時間 / 得獎名稱）', verbose_name='指導學生之特殊榮譽'),
        students_conference = models.TextField(blank=True, default='', help_text='主辦及參與國際會議（時間 / 會議名稱）', verbose_name='主辦及參與國際會議'),
    )
    
    edit_time = models.DateField(auto_now=True)
    
    # Metadata
    class Meta:
        verbose_name_plural = '師資'
        ordering = ['order', 'place']

    # Methods
    def  get_absolute_url(self):
        return reverse('members-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

##########################系辦成員##########################
class Office_Member(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=20, help_text='姓名', verbose_name='姓名'),
        position = models.CharField(max_length=100, help_text='職位', verbose_name='職位'),
        resbonsibility = models.CharField(max_length=50, help_text = '負責業務', verbose_name='負責業務'),
    )
    email = models.EmailField(help_text = '信箱', verbose_name='信箱')
    phone = models.CharField(max_length=50, help_text='電話', verbose_name='電話')
    photo = models.ImageField(upload_to='images/member/office', blank=True, null=True, verbose_name='照片')
    edit_time = models.DateField(auto_now=True)

    # Metadata
    class Meta:
        # ordering = ['name']
        verbose_name_plural = '系辦成員'

    # Methods
    def get_absolute_url(self):
        return reverse('office_members-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
