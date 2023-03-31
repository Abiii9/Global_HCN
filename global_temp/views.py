from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature
# Create your views here.

Month_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']


def get_year_list(request):
    if 'year_list' in request.session:
        years = request.session['year_list']
    else:
        years = list(Year.objects.values_list('year', flat=True))
        request.session['year_list'] = years
    return years

def year_list(request):
    years = get_year_list(request)
    return render(request, 'global_temp/index.html', {'years': years})

def get_temperatures(request,year,month):
    if str(year)+'_'+month in request.session:
        temps = request.session[str(year)+'_'+month]
    else:
        year_obj = Year.objects.filter(year=year).first()
        temps = list(Temperature.objects.filter(year=year_obj.id, month=month).values())
        request.session[str(year)+'_'+month] = temps
    return temps

def temp_detail(request):
    try:
        years = get_year_list(request)
        year = '2000'
        month = '1'
        if request.method == "POST":
            year = request.POST.get('year')
            month = request.POST.get('monthID')
        temps = get_temperatures(request, year, month)
        return render(request, 'global_temp/temperature_details.html', {'years':years, 'lst':Month_list[int(month)], 'temp': temps, 'yr':year, 'month':month, 'longitude_range': range(5,185,5)})
    except:
        #returning a custom 400 error template incase of a bad request.
        return render(request, 'global_temp/400.html')


def map_detail(request, year, month):
    #This function gets the year and month values as inputs from the temperature_details page and renders the map view using leaflet,
    #where the temperature variations are displayed in degree celsius, for every location on map.
    try:
        #fetching the query set containing temperature data of all locations for a particular year and month.
        temps = get_temperatures(request,year,month)
        #creating a list from the query set.
        res_temps = [temp for temp in temps]
        #passing the values of temperature to be rendered on map, along with year and month.
        return render(request, 'global_temp/map.html', {'temps': res_temps, 'yr':year, 'month':month, 'month_name':Month_list[int(month)]})
    except:
        #returning a custom 400 error template incase of a bad request.
        return render(request, 'global_temp/400.html')
def chart_processing(request):
    try:
        chart_data = []
        chart_data2 =[]
        if request.method == "POST":
            latitude = request.POST.get('latitude', '')
            month = request.POST.get('month', '')
            longitude = "lon_"+request.POST.get('longitude', '')
            if latitude+'_'+month+'_temps' in request.session:
                temp_data = request.session[latitude+'_'+month+'_temps']
            else:
                temp_data = list(Temperature.objects.filter(latitude=latitude, month=month).values())
                request.session[latitude+'_'+month+'_temps'] = temp_data
            for temp in temp_data:
                chart_data.append(temp[longitude]/100)
            if request.POST.get('button','') == 'compare':
                latitude2 = request.POST.get('latitude2', '')
                month2 = request.POST.get('month2', '')
                longitude2 = "lon_" + request.POST.get('longitude2', '')
                if latitude2 + '_' + month2 + '_temps' in request.session:
                    temp_data2 = request.session[latitude2 + '_' + month2 + '_temps']
                else:
                    temp_data2 = list(Temperature.objects.filter(latitude=latitude, month=month).values())
                    request.session[latitude2 + '_' + month2 + '_temps'] = temp_data2
                for temp in temp_data2:
                    chart_data2.append(temp[longitude2] / 100)
                return render(request, 'global_temp/charts.html',
                              {'data_list': chart_data, 'data_list2': chart_data2, 'latitude': latitude,
                               'longitude': longitude, 'month': Month_list[int(month)], 'latitude2': latitude2,
                               'longitude2': longitude2, 'month2': Month_list[int(month2)],
                               'latitude_range': range(5, 95, 5), 'longitude_range': range(5, 185, 5)})

            return render(request,'global_temp/charts.html', {'data_list': chart_data,'data_list2': chart_data2, 'latitude': latitude, 'longitude': longitude, 'month': Month_list[int(month)], 'latitude_range': range(5,95,5), 'longitude_range': range(5,185,5)})
        else:
            return render(request, 'global_temp/charts.html',{'data_list': chart_data,'data_list2': chart_data2,'latitude_range': range(5,95,5), 'longitude_range': range(5,185,5)})
    except:
        #returning a custom 400 error template incase of a bad request.
        return render(request, 'global_temp/400.html')

def about(request):
    return render(request, 'global_temp/about.html')

def temperature_details(request):
    return render(request, 'global_temp/temperature_details.html')

#function that gets called incase of a 404 page not found error.
def error_404_view(request, exception):
    return render(request, 'global_temp/404.html')
#function that gets called incase of a 500 internal server error.
def error_500_view(request):
    return render(request, 'global_temp/500.html')