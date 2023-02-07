from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Other(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
        image = models.ImageField(upload_to='images/other', null=True, blank=True),
        link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
    )
    
    #Metadata
    class Meta:
        # ordering = ['date']
        verbose_name_plural = '其他服務系統'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('others-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

# class NCKU(TranslatableModel):
#     #Fields
#     translations = TranslatedFields(
#         title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
#         content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
#         date = models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
#         image = models.ImageField(null=True, blank=True),
#         link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
#     )

#     #Metadata
#     class Meta:
#         # ordering = ['date']
#         verbose_name_plural = '成功大學'

#     #Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of the model."""
#         return reverse('ncku-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.title

# class EECS(TranslatableModel):
#     #Fields
#     translations = TranslatedFields(
#         title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
#         content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
#         date = models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
#         image = models.ImageField(null=True, blank=True),
#         link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
#     )
    
#     #Metadata
#     class Meta:
#         # ordering = ['date']
#         verbose_name_plural = '電資學院'

#     #Methods
#     def get_absolute_url(self):
#         """Returns the url to access a particular instance of the model."""
#         return reverse('eecs-detail-view', args=[str(self.id)])

#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.title

class Alumni(TranslatableModel):
    #Fields
    translations = TranslatedFields(
        title = models.CharField(max_length=200, help_text='輸入標題', blank=True, verbose_name='標題'),
        content = models.TextField(help_text='輸入內容',blank=True, verbose_name='內容'),
        date = models.DateTimeField(auto_now_add=True, verbose_name='圖片'),
        image = models.ImageField(null=True, blank=True),
        link = models.URLField(max_length=200, help_text='輸入連結網址',null=True, blank=True, verbose_name='相關連結'),
    )

    #Metadata
    class Meta:
        # ordering = ['date']
        verbose_name_plural = '系友資訊'

    #Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('alimni-detail-view', args=[str(self.id)])

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