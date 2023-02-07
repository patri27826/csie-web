from django.db import models
from django.urls import reverse
import os
import django.utils.timezone as timezone
from datetime import datetime

# Create your models here.
class Post(models.Model):

    #Fields
    title = models.CharField(max_length=200, help_text='輸入標題', verbose_name='公告標題')
    title_en = models.CharField(max_length=200, help_text='輸入英文標題(非必填)', null=True, blank=True, verbose_name='英文公告標題')
    content = models.TextField(help_text='輸入內容', verbose_name='公告內容')
    content_en = models.TextField(help_text='輸入英文內容(非必填)', null=True, blank=True, verbose_name='英文公告內容')
    type = models.ManyToManyField('Type', verbose_name='公告類型')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='公告狀態')
    staff = models.CharField(max_length=50, help_text='輸入人員', verbose_name='公告人員')
    date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='公告日期')
    update_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='更新日期')
    is_pin = models.BooleanField(default=False, verbose_name='置頂')
    
    link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結')

    #Metadata
    class Meta:
        ordering = ['-is_pin', '-update_date', '-date']
        verbose_name_plural = '公告'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('post-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title


class Type(models.Model):

    name = models.CharField(max_length=20, help_text='Enter a post type')

    class Meta:
        ordering = ['name']
        verbose_name_plural = '公告類型'

    def get_absolut_url(self):
        return reverse('type-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Status(models.Model):

    NORMAL = '一般'
    IMPORTANT = '重要'
    BACHELOR = '大學部'
    MASTER = '碩士'
    PhD = '博士'
    GRADUATE = '畢業生'

    STATUS_CHOICES = (
        (NORMAL, '一般'),
        (IMPORTANT, '重要'),
        (BACHELOR, '大學部'),
        (MASTER, '碩士'),
        (PhD, '博士'),
        (GRADUATE, '畢業生')
    )
    name = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NORMAL,
    )
    # name = models.CharField(max_length=10, help_text='Enter a post status')
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = '公告狀態'

    def get_absolut_url(self):
        return reverse('status-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class PostFile(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # When a Case is deleted, upload models are also deleted
    file = models.FileField(upload_to='post/files/', null = True, blank = True, verbose_name='附加檔案')

    class Meta:
        verbose_name_plural = '附加檔案'

    def __str__(self):
        return os.path.basename(self.file.name)

class PostImage(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE) # When a Case is deleted, upload models are also deleted
    image = models.FileField(upload_to='post/images/', null = True, blank = True, verbose_name='附加圖片')

    class Meta:
        verbose_name_plural = '附加圖片'

    def __str__(self):
        return os.path.basename(self.image.name)