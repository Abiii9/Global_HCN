from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature

#creating a list of month names
Month_list = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
       'December']


def get_year_list(request):
    #This helper function is used to get the list of years from the Year model.
    #check if the year_list is present in the session, to avoid querying the database.
    if 'year_list' in request.session:
        years = request.session['year_list']
    else:
        #fetching values from the Year model.
        years = list(Year.objects.values_list('year', flat=True))
        request.session['year_list'] = years
    return years

def year_list(request):
    #This function is used to send the list of years to the index page of the application.
    years = get_year_list(request)
    return render(request, 'global_temp/index.html', {'years': years})

def get_temperatures(request,year,month):
    #this helper function is used to get the temperature data from the temperature model, by filtering it
    #using the year and month received from the form input.

    #check if the year and month values are present in the session, to avoid querying the database.
    if str(year)+'_'+month in request.session:
        temps = request.session[str(year)+'_'+month]
    else:
        #fetching the year object from the Year model
        year_obj = Year.objects.filter(year=year).first()
        #fetching the temperature object that matches with the filter conditions.
        temps = list(Temperature.objects.filter(year=year_obj.id, month=month).values())
        request.session[str(year)+'_'+month] = temps
    return temps

def temp_detail(request):
    #This function is used to fetch and display the temperature values from the database and passing it
    #to the render function as arguments.
    try:
        #assigning default values for the year and month.
        years = get_year_list(request)
        year = '2000'
        month = '1'
        #checking if the request received is a POST request, assigning the values given by the user
        #to variables and sending them to the get_temperatures method.
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
    #This function is used to display a chart representation of the temperature variations in a location point
    #over the years 2000 - 2014.
    try:
        #initializing chart_data variables to an empty list.
        chart_data = []
        chart_data2 =[]
        #if the POST request is received from the user, get the temperature data for the latitude and longitude values
        #specified by the user. 
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
            #if the user wants to compare the temperature variations of two locations,
            #fetch the values of the second location and get the temperature data accordingly.
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
            #if there is no POST request, send the data without latitude and longitude, which will be received from a point clicked on the map.
            return render(request, 'global_temp/charts.html',{'data_list': chart_data,'data_list2': chart_data2,'latitude_range': range(5,95,5), 'longitude_range': range(5,185,5)})
    except:
        #returning a custom 400 error template incase of a bad request.
        return render(request, 'global_temp/400.html')

def about(request):
    #this function renders the about page of the website.
    return render(request, 'global_temp/about.html')

def temperature_details(request):
    #this function renders the temperature_details page of the website, from the navigation bar.
    return render(request, 'global_temp/temperature_details.html')

#function that gets called incase of a 404 page not found error.
def error_404_view(request, exception):
    return render(request, 'global_temp/404.html')
#function that gets called incase of a 500 internal server error.
def error_500_view(request):
    return render(request, 'global_temp/500.html')