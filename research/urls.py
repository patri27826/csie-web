from django.urls import path
from . import views


urlpatterns = [
    path('lab', views.lab, name='Lab'),
    path('areas', views.areas, name='Areas'),
    path('centers', views.centers, name='Centers'),
    path('international', views.international, name='International'),
]