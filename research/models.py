from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Areas(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, blank=True),
        # image = models.ImageField(null=True, blank=True),
    )
    
    #Metadata
    class Meta:
        # ordering = ['date']
        verbose_name_plural = '研究群'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('areas-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

class Centers(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, blank=True),
        link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
    )
    
    #Metadata
    class Meta:
        # ordering = ['date']
        verbose_name_plural = '研究中心'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('centers-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

class International(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, blank=True),
        # image = models.ImageField(null=True, blank=True),
        # link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
    )

    #Metadata
    class Meta:
        # ordering = ['-title']
        verbose_name_plural = '國際合作交流'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('courseinfo-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title