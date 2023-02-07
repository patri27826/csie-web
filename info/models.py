from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.
class Info(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', verbose_name='大標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        subtitle1 = models.TextField(max_length=200, help_text='輸入小標題',blank=True, verbose_name='小標題一'),
        subcontent1 = models.TextField(help_text='輸入內容',blank=True, verbose_name='小標題一內容'),
        subtitle2 = models.TextField(max_length=200, help_text='輸入小標題',blank=True, verbose_name='小標題二'),
        subcontent2 = models.TextField(help_text='輸入內容',blank=True, verbose_name='小標題二內容'),
        subtitle3 = models.TextField(max_length=200, help_text='輸入小標題',blank=True, verbose_name='小標題三'),
        subcontent3 = models.TextField(help_text='輸入內容',blank=True, verbose_name='小標題三內容'),
        # image = models.ImageField(null=True, blank=True)
    )
    

    #Metadata
    class Meta:
        # ordering = ['-title']
        verbose_name_plural = '系所介紹'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('info-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title
        
class TextInfo(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
    )
    type = models.ManyToManyField('Type', verbose_name='類型')
    
    #Metadata
    class Meta:
        verbose_name_plural = '文字資訊'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('centers-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

class Type(models.Model):

    name = models.CharField(max_length=20, help_text='Enter a post type')

    class Meta:
        ordering = ['name']
        verbose_name_plural = '資訊類型'

    def get_absolut_url(self):
        return reverse('type-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Visiting(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
        image = models.ImageField(upload_to='images/info/visiting', null=True, blank=True),
    )
    
    #Metadata
    class Meta:
        # ordering = ['date']
        verbose_name_plural = '交通資訊'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('visitinginfo-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

# class Venue(models.Model):
#     #Fields
#     title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題')
#     content = models.TextField(max_length=1000, help_text='輸入內容',blank=True, verbose_name='內容')
#     date = models.DateTimeField(auto_now_add=True, verbose_name='圖片')
#     image = models.ImageField(null=True, blank=True)

#     #Metadata
#     class Meta:
#         ordering = ['date']
#         verbose_name_plural = '場地租借'

#     #Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of the model."""
#         return reverse('venue-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.title

# class Equipment(models.Model):
#     #Fields
#     title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題')
#     content = models.TextField(max_length=1000, help_text='輸入內容',blank=True, verbose_name='內容')
#     date = models.DateTimeField(auto_now_add=True, verbose_name='圖片')
#     image = models.ImageField(null=True, blank=True)
#     link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結')


#     #Metadata
#     class Meta:
#         ordering = ['date']
#         verbose_name_plural = '設備介紹'

#     #Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of the model."""
#         return reverse('venue-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.title

from django.forms import ModelForm, Textarea