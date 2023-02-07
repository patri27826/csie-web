from django.urls import path
from . import views
from haystack.views import SearchView
from django.urls import include, re_path

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.PostListView.as_view(), name='posts'),
    path('normal', views.PostListView_1.as_view(), name='posts_normal'),
    path('bachelorAdmission', views.PostListView_bachelorAdmission.as_view(), name='posts_bachelorAdmission'),
    path('masterAdmission', views.PostListView_masterAdmission.as_view(), name='posts_masterAdmission'),
    path('speeches', views.PostListView_3.as_view(), name='posts_speeches'),
    path('awards', views.PostListView_4.as_view(), name='posts_awards'),
    path('scholarship', views.PostListView_5.as_view(), name='posts_scholarship'),
    path('jobs', views.PostListView_6.as_view(), name='posts_jobs'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail-view'),
    re_path(r'^search/$', views.globalsearch.as_view(), name='search'),
    # re_path(r'hs_search/$', SearchView(), name='haystack_search'),
]