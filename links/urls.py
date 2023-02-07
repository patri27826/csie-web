from django.urls import path
from . import views


urlpatterns = [
    path('other', views.other, name='Other'),
    path('alumni', views.alumni, name='Alumni'),
    path('venue', views.venue, name='Venue'),
]