from django.shortcuts import render, get_object_or_404
from .models import Year,Temperature
# Create your views here.

def year_list(request):
    global years
    years = Year.objects.all()
    return render(request, 'global_temp/index.html', {'years': years})

# def temp_detail(request):
# #temps = get_object_or_404(Temperature, year=year)
#     temps = Temperature.objects.filter(year=yearID, month=monthID).values()
#     resTemps = []
#     for temp in temps:
#         resTemps.append(temp)
#     print(resTemps)
#     return render(request, 'global_temp/temp.html', {'temps': resTemps})

def temp_detail(request):
    if request.method=="POST":
        yearID = request.POST.get('yearID')
        monthID = request.POST.get('monthID')
        temps = Temperature.objects.filter(year=yearID, month=monthID).values()
        yr = Year.objects.filter(id=yearID)
        resTemps = [temp for temp in temps]
    return render(request, 'global_temp/temp.html', {'temps': resTemps, 'yr':yr, 'month':monthID})

