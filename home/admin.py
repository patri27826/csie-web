from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin
# Register your models here.
from .models import Carousel, Image, Link, ITNews, homeInfo, homeImage, externalLink
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ITNewsResource(resources.ModelResource):
    class Meta:
        model = ITNews

class externalLinkResource(resources.ModelResource):
    class Meta:
        model = externalLink

admin.site.register(Carousel)
admin.site.register(Image)

@admin.register(Link)
class externalLinkAdmin(admin.ModelAdmin):
    list_display = ('text', 'link')

@admin.register(ITNews)
class ITNewsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'link')

@admin.register(externalLink)
class externalLinkAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ('name', 'link')

@admin.register(homeInfo)
class homeInfoAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title','content',)
    summernote_fields = ('content',)

@admin.register(homeImage)
class homeInfoAdmin(TranslatableAdmin):
    pass

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'