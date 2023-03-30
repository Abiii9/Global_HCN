from django.urls import path
from . import views

urlpatterns = [
    path('', views.year_list, name='year_list'),
    path('about', views.about, name = 'about' ),
    path('temp/details/', views.temp_detail, name='temp_detail'),
    path('temp/map/<int:year>/<str:month>', views.map_detail, name='map_detail'),
    path('temp/charts/', views.chart_processing, name='chart_processing'),]
    
