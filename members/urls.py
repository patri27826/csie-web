from django.urls import path
from . import views

from locallibrary.settings import MEDIA_ROOT
from django.views.static import serve

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.MemberListView.as_view(), name='members'),
    path('csie', views.MemberListView_csie.as_view(), name='members_csie'),
    path('csieg', views.MemberListView_csieg.as_view(), name='members_csieg'),
    path('ai', views.MemberListView_ai.as_view(), name='members_ai'),
    path('med', views.MemberListView_med.as_view(), name='members_med'),
    path('imis', views.MemberListView_imis.as_view(), name='members_imis'),
    path('adjunct', views.MemberListView_adjunct.as_view(), name='members_adjunct'),
    path('joint', views.MemberListView_joint.as_view(), name='members_joint'),
    path('visiting', views.MemberListView_visiting.as_view(), name='members_visiting'),
    path('retire', views.MemberListView_retire.as_view(), name='members_retired'),
    path('<int:pk>', views.MemberDetailView.as_view(), name='members-detail-view'),     # 命名變量,eg 'catalog/<id>/'
    path('office_members/', views.OfficeMemberListView.as_view(), name='office_members'),
    path('office_member/<int:pk>', views.OfficeMemberDetailView.as_view(), name='office_member_detail'),
]