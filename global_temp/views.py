from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature
# Create your views here.

def year_list(request):
    global years
    years = Year.objects.all()
    return render(request, 'global_temp/index.html', {'years': years})

def temp_detail(request):
    if request.method=="POST":
        year = request.POST.get('year')
        year_obj = Year.objects.filter(year=year).first()
        monthID = request.POST.get('monthID')
        lst = ['', 'January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
        temps = Temperature.objects.filter(year=year_obj.id, month=monthID).values()
        
    return render(request, 'global_temp/temperature_details.html', {'lst':lst[int(monthID)], 'temp': temps, 'yr':year, 'month':monthID})


def map_detail(request, year, month):
    
    year_obj = Year.objects.filter(year=year).first()
    temps = Temperature.objects.filter(year=year_obj.id, month=month).values()
    resTemps = [temp for temp in temps]
    return render(request, 'global_temp/temp.html', {'temps': resTemps, 'yr':year, 'month':month})

