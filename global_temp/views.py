from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature
# Create your views here.

def year_list(request):
    years = Year.objects.all()
    return render(request, 'global_temp/index.html', {'years': years})

def temp_detail(request, yearID):
    #temps = get_object_or_404(Temperature, year=year)
    temps = Temperature.objects.filter(year=yearID)
    return render(request, 'global_temp/temp.html', {'temps': temps})

