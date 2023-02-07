from django.contrib import admin

# Register your models here.
from .models import Info, TextInfo, Type, Visiting
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin

@admin.register(Info)
class InfoAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    summernote_fields = ('content', 'subcontent1', 'subcontent2', 'subcontent3')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TextInfo)
class TextInfoAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    list_filter = ('type',)
    summernote_fields = ('content',)

@admin.register(Visiting)
class VisitAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title', 'content', 'image')
    summernote_fields = ('content',)

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'
