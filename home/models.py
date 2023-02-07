from django.db import models
from django.forms import ModelForm
from django.urls import reverse
import os
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Carousel(models.Model):

    #Fields
    csie = models.ImageField(upload_to='images/home/carousel',null=True, blank=True, verbose_name='系上形象圖片')
    other = models.ManyToManyField('Image', verbose_name='其他圖片')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')

    #Metadata
    class Meta:
        ordering = ['-date']
        verbose_name_plural = '頁首輪播'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('csiepicture-detail-view', args=[str(self.id)])
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return '頁首輪播'

class Image(models.Model):

    #Fields
    image = models.ImageField(upload_to='images/home/carousel',null=True, blank=True, verbose_name='圖片')
    description = models.TextField(max_length=100, help_text='輸入內容', null=True, blank=True, verbose_name='圖片描述')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')

    #Metadata
    class Meta:
        ordering = ['-date']
        verbose_name_plural = '輪播圖片上傳'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('carousel-detail-view', args=[str(self.id)])
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return os.path.basename(self.image.name)


class Link(models.Model):
    
    text = models.CharField(max_length=50, default="", verbose_name='顯示文字')
    link = models.URLField(null=True, blank=True, verbose_name='連結網址')

    #Metadata
    class Meta:
        verbose_name_plural = '快速連結'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('navbar-detail-view', args=[str(self.id)])
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.link

class ITNews(models.Model):

    #Fields
    title = models.CharField(max_length=200, help_text='輸入標題', verbose_name='標題')
    date = models.DateTimeField(auto_now_add=True, verbose_name='日期')
    image = models.ImageField(upload_to='images/home/ITnews',null=True, blank=True, verbose_name='圖片')
    link = models.URLField(help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結')

    class Meta:
        ordering = ['-date']
        verbose_name_plural = '資訊要聞'
    
    def get_absolut_url(self):
        return reverse('itnews-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class homeInfo(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', verbose_name='標題'),
        content = models.TextField(help_text='輸入內容', verbose_name='內容'),
        image = models.ImageField(upload_to='images/home/homeInfo',null=True, blank=True, verbose_name='圖片'),
        link = models.URLField(help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
    )

    class Meta:
        verbose_name_plural = '文字訊息'
    
    def get_absolut_url(self):
        return reverse('homeinfo-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class homeImage(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        image = models.ImageField(upload_to='images/home/homeImage', verbose_name='圖片')
    )

    class Meta:
        verbose_name_plural = '地圖'
    
    def get_absolut_url(self):
        return reverse('homeimage-detail', args=[str(self.id)])

    def __str__(self):
        return os.path.basename(self.image.name)

class externalLink(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, help_text='輸入名稱', verbose_name='名稱'),
        description = models.TextField(help_text='輸入內容', null=True, blank=True, verbose_name='圖片描述'),
    )
    icon = models.ImageField(upload_to='images/home/icon', verbose_name='圖片')
    link = models.URLField(help_text='輸入連結網址', verbose_name='相關連結')

    class Meta:
        verbose_name_plural = '外部相關連結'
    
    def get_absolut_url(self):
        return reverse('externallink-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Visit(models.Model):
    times = models.IntegerField()