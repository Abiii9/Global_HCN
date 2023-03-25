from django.urls import path
from . import views

urlpatterns = [
    path('', views.year_list, name='year_list'),
    path('temp/', views.temp_detail, name='temp_detail'),
    path('temperature_details/', views.temp_detail, name='temp_detail'),
    
]
