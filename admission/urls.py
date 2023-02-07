from django.urls import path
from . import views


urlpatterns = [
    path('senior', views.adm_senior, name='adm_senior'),
    path('bachelor', views.adm_bachelor, name='adm_bachelor'),
    path('bs', views.adm_bs, name='adm_bs'),
    path('talent', views.adm_talent, name='adm_talent'),
    path('csie', views.adm_CSIE, name='adm_CSIE'),
    path('imi', views.adm_imi, name='adm_imi'),
    path('ai', views.adm_ai, name='adm_ai'),
    path('industrial', views.adm_industrial, name='adm_industrial'),
    path('in-service', views.adm_inService, name='adm_inService'),
]