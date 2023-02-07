"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
# Use include() to add URLS from the catalog application and authentication system
from django.urls import include
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap, MemberSitemap, StaticViewSitemap


urlpatterns = [
    path('admin/', admin.site.urls),
]

sitemaps = {
    'post': PostSitemap,
    'member': MemberSitemap,
    'static': StaticViewSitemap,
}

urlpatterns += [
    # path('catalog/', include('catalog.urls')),
    path('ncku_csie/', include('home.urls')),
    path('news/', include('news.urls')),
    path('members/', include('members.urls')),
    path('info/', include('info.urls')),
    path('home/', include('home.urls')),
    path('education/', include('education.urls')),
    path('admission/', include('admission.urls')),
    path('research/', include('research.urls')),
    path('links/', include('links.urls')),
    path('alumni_area/', include('alumni_area.urls')),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]



#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('rosetta/', include('rosetta.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

X_FRAME_OPTIONS = 'SAMEORIGIN'

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('news/', include('news.urls')),
    path('members/', include('members.urls')),
    path('info/', include('info.urls')),
    path('home/', include('home.urls')),
    path('education/', include('education.urls')),
    path('admission/', include('admission.urls')),
    path('research/', include('research.urls')),
    path('links/', include('links.urls')),
    path('alumni_area/', include('alumni_area.urls')),
    path('', include('home.urls')),
    path('ncku_csie/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)