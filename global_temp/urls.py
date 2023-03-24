from django.urls import path
from . import views

urlpatterns = [
    path('', views.year_list, name='year_list'),
    path('temp/<int:yearID>/', views.temp_detail, name='temp_detail'),
    
]