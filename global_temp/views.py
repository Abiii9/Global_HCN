from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature
# Create your views here.

Month_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']


def year_list(request):
    years = Year.objects.all()
    return render(request, 'global_temp/index.html', {'years': years})

def temp_detail(request):
    if request.method=="POST":
        year = request.POST.get('year')
        year_obj = Year.objects.filter(year=year).first()
        monthID = request.POST.get('monthID')
        temps = Temperature.objects.filter(year=year_obj.id, month=monthID).values()
    return render(request, 'global_temp/temperature_details.html', { 'lst':Month_list[int(monthID)], 'temp': temps, 'yr':year, 'month':monthID, 'longitude_range': range(5,185,5)})


def map_detail(request, year, month):
    
    year_obj = Year.objects.filter(year=year).first()
    temps = Temperature.objects.filter(year=year_obj.id, month=month).values()
    resTemps = [temp for temp in temps]
    return render(request, 'global_temp/temp.html', {'temps': resTemps, 'yr':year, 'month':month})

def chart_processing(request):
    if request.method == "POST":
        latitude = request.POST.get('latitude', '')
        month = request.POST.get('month', '')
        longitude = "lon_"+request.POST.get('longitude', '')
        temps = Temperature.objects.filter(latitude=latitude, month=month)
        data = []

        for temp in temps:
            data.append(getattr(temp, longitude))

        return render(request,'global_temp/charts.html', {'data_list': data, 'latitude': latitude, 'longitude': longitude, 'month': Month_list[int(month)], 'latitude_range': range(5,95,5), 'longitude_range': range(5,185,5)})
    else:
        return render(request, 'global_temp/charts.html',{'latitude_range': range(5,95,5), 'longitude_range': range(5,185,5)})
