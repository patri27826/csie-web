from django.urls import path
from . import views


urlpatterns = [
    path('', views.InfoListView.as_view(), name='info'),
    path('directions', views.directions, name='Directions'),
    path('honor', views.honor, name='Honor'),
    path('regulation', views.regulation, name='Regulation'),
    path('visiting', views.visiting, name='Visiting'),
    path('equipment', views.equipment, name='Equipment'),
]