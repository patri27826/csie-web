from django.urls import path
from . import views


urlpatterns = [
    path('', views.courseInfo, name='CourseInfo'),
    path('credits', views.credits, name='Credits'),
    path('bachelor', views.bachelor, name='Bachelor'),
    path('bs', views.bs, name='BS'),
    path('instCSIE', views.instCSIE, name='instCSIE'),
    path('imi', views.imi, name='IMI'),
    path('ai', views.ai, name='AI'),
    path('industrial', views.industrial, name='Industrial'),
    path('inService', views.inService, name='inService'),
    path('documents', views.documents, name='Documents'),
]