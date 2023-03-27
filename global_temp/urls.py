from django.urls import path
from . import views

urlpatterns = [
    path('', views.year_list, name='year_list'),
    path('temperature_details/', views.temp_detail, name='temp_detail'),
    path('map/<int:year>/<int:month>', views.map_detail, name='map_detail'),]
    
