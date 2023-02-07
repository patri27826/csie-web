from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from parler.admin import TranslatableAdmin
# Register your models here.
from .models import Areas, Centers, International

@admin.register(Areas)
class AreasAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title', 'content')
    summernote_fields = ('content',)

@admin.register(Centers)
class CentersAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title', 'content')
    summernote_fields = ('content',)

@admin.register(International)
class InternationalAdmin(TranslatableAdmin, SummernoteModelAdmin):
    list_display = ('title', 'content')
    summernote_fields = ('content',)


# admin.site.register(Areas, AreasAdmin)
# admin.site.register(Centers, AreasAdmin)

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'