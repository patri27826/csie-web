from django.contrib import admin

# Register your models here.
from .models import Post, Type, Status, PostFile, PostImage
from django_summernote.admin import SummernoteModelAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        

class StatusAdmin(admin. ModelAdmin):
    pass
admin.site.register(Status, StatusAdmin)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ('status', 'title', 'type', 'date')
#     # list_filter = ('status', 'type')

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'

class PostFileAdmin(admin.StackedInline):
    model = PostFile
class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin, ImportExportModelAdmin):
    inlines = [PostFileAdmin,PostImageAdmin]
    list_display = ('title', 'date', 'update_date')
    list_filter = ('status', 'type')
    search_fields = ('title', 'status__name', 'type__name', 'content', 'staff', 'date', 'title_en', 'content_en')
    fields = ['title', 'title_en', ('content', 'content_en'), 'is_pin', ('type', 'status'), ('date', 'update_date'), 'staff', 'link']
    summernote_fields = ('content', 'content_en')

@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    pass
@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass