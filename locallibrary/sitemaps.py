from django.contrib import sitemaps
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from news.models import Post
from members.models import Member

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.update_date

class MemberSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Member.objects.all()
    def lastmod(self, obj):
        return obj.edit_time

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home',
            'posts',
            'posts_normal',
            'posts_bachelorAdmission',
            'posts_masterAdmission',
            'posts_speeches',
            'posts_awards',
            'posts_scholarship',
            'posts_jobs',
            'members',
            'members_csie',
            'members_csieg',
            'members_ai',
            'members_imis',
            'members_med',
            'members_adjunct',
            'members_joint',
            'members_visiting',
            'members_retired',
            'office_members',
            'info','Directions','Honor','Regulation','Visiting',
            'Credits','Bachelor','BS','instCSIE','IMI','AI','Industrial','inService','Documents',
            'adm_senior','adm_bachelor','adm_bs','adm_talent','adm_CSIE','adm_imi','adm_ai','adm_industrial','adm_inService',
            'Lab','Areas','Centers','International',
            'Other','Alumni','Venue',
            ]

    def location(self, item):
        return reverse(item)