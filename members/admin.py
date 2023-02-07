from django.contrib import admin
# Register your models here.
# from .models import Honor, Member, Office_Member, Department, Patent, Project, Published, Student_Conference, Student_Honor, Student_Name
from .models import Member, Office_Member, Department, Classification
from django_summernote.admin import SummernoteModelAdmin
from django.utils.translation import gettext_lazy as _
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from parler.admin import TranslatableAdmin
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user

class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class Office_MemberResource(resources.ModelResource):
    class Meta:
        model = Office_Member

# class ClassificationFilter(admin.SimpleListFilter):
#     # Human-readable title which will be displayed in the
#     # right admin sidebar just above the filter options.
#     title = _('分類')

#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = 'classifications'

#     def lookups(self, request, model_admin):
#         """
#         Returns a list of tuples. The first element in each
#         tuple is the coded value for the option that will
#         appear in the URL query. The second element is the
#         human-readable name for the option that will appear
#         in the right sidebar.
#         """
#         return (
#             ('Full_time', _('專任')),
#             ('Adjunct', _('兼任')),
#             ('Joint', _('合聘')),
#             ('Visiting', _('客座')),
#             ('Retired', _('退休')),
#         )

#     def queryset(self, request, queryset):
#         """
#         Returns the filtered queryset based on the value
#         provided in the query string and retrievable via
#         `self.value()`.
#         """
#         # Compare the requested value (either '80s' or '90s')
#         # to decide how to filter the queryset.
#         if self.value() == 'Full_time':
#             return queryset.filter(
#                 classification__contains='Full_time'
#             )
#         if self.value() == 'Adjunct':
#             return queryset.filter(
#                 classification__contains='Adjunct'
#             )
#         if self.value() == 'Joint':
#             return queryset.filter(
#                 classification__contains='Joint'
#             )
#         if self.value() == 'Visiting':
#             return queryset.filter(
#                 classification__contains='Visiting'
#             )
#         if self.value() == 'Retired':
#             return queryset.filter(
#                 classification__contains='Retired'
#             )
@admin.register(Member)
class MemberAdmin(TranslatableAdmin, GuardedModelAdmin, SummernoteModelAdmin, ImportExportModelAdmin):
    change_form_template = 'admin/members/member/change_form.html'
    list_display = ('name', 'edit_time')
    list_filter = ('place', 'department', 'classification',)
    search_fields = ('name', 'place', 'department__name')
    summernote_fields = ('expertise', 'graduate', 'experience', 'patent', 'awarded', 'published_accepted_papers', 'published_refered_papers', 'published_conference_foreign', 'published_conference_domestic', 'project_tech', 'project_gen', 'students_doc', 'students_master', 'students_honor', 'students_conference')
    
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        data = self.get_model_objects(request)
        return data

    def get_model_objects(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view','edit','delete']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions], klass=klass, any_perm=True)

    def has_permission(self, request, obj, action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else:
            return self.get_model_objects(request).exists()

    def has_view_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'view')

    def has_change_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'change')

    def has_delete_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'delete')

@admin.register(Office_Member)
class Office_MemberAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ('name', 'position', 'edit_time')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'edit_time')

@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'edit_time')

admin.site.site_header = '後臺管理系統'    
admin.site.site_title = '後臺管理'
admin.site.index_title = '後臺站點管理'
