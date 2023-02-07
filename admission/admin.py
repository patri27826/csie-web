from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin
# Register your models here.
from .models import TextInfo, Type

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(TextInfo)
class TextInfoAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title',)
    list_filter = ('type',)
    summernote_fields = ('content',)

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'