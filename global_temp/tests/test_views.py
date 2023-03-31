from django.test import Client, TestCase
from global_temp.models import Year, Temperature
from django.shortcuts import reverse
from global_temp.views import get_temperatures

class TemeratureViewTests(TestCase):
    @classmethod
    #setting up test data for the Year Model
    def setUpTestData(cls):
        Year.objects.create(year = 2000)
        Year.objects.create(year = 2001)
        Year.objects.create(year = 2002)
        year_obj1 = Year.objects.get(id=1)
        Temperature.objects.create(
            year=year_obj1,
            latitude='30-35S',
            month=1, 
            lon_175_180W = 2.5,
            lon_170_175W = 2.5,
            lon_165_170W = 2.5,
            lon_160_165W = 2.5,
            lon_155_160W = 2.5,
            lon_150_155W = 2.5,
            lon_145_150W = 2.5,
            lon_140_145W = 2.5,
            lon_135_140W = 2.5,
            lon_130_135W = 2.5,
            lon_125_130W = 2.5,
            lon_120_125W = 2.5,
            lon_115_120W = 2.5,
            lon_110_115W = 2.5,
            lon_105_110W = 2.5,
            lon_100_105W = 2.5,
            lon_95_100W = 2.5,
            lon_90_95W = 2.5,
            lon_85_90W = 2.5,
            lon_80_85W = 2.5,
            lon_75_80W = 2.5,
            lon_70_75W = 2.5,
            lon_65_70W = 2.5,
            lon_60_65W = 2.5,
            lon_55_60W = 2.5,
            lon_50_55W = 2.5,
            lon_45_50W = 2.5,
            lon_40_45W = 2.5,
            lon_35_40W = 2.5,
            lon_30_35W = 2.5,
            lon_25_30W = 2.5,
            lon_20_25W = 2.5,
            lon_15_20W = 2.5,
            lon_10_15W = 2.5,
            lon_5_10W = 2.5,
            lon_0_5W = 2.5,

            lon_175_180E = 2.5,
            lon_170_175E = 2.5,
            lon_165_170E = 2.5,
            lon_160_165E = 2.5,
            lon_155_160E = 2.5,
            lon_150_155E = 2.5,
            lon_145_150E = 2.5,
            lon_140_145E = 2.5,
            lon_135_140E = 2.5,
            lon_130_135E = 2.5,
            lon_125_130E = 2.5,
            lon_120_125E = 2.5,
            lon_115_120E = 2.5,
            lon_110_115E = 2.5,
            lon_105_110E = 2.5,
            lon_100_105E = 2.5,
            lon_95_100E = 2.5,
            lon_90_95E = 2.5,
            lon_85_90E = 2.5,
            lon_80_85E = 2.5,
            lon_75_80E = 2.5,
            lon_70_75E = 2.5,
            lon_65_70E = 2.5,
            lon_60_65E = 2.5,
            lon_55_60E = 2.5,
            lon_50_55E = 2.5,
            lon_45_50E = 2.5,
            lon_40_45E = 2.5,
            lon_35_40E = 2.5,
            lon_30_35E = 2.5,
            lon_25_30E = 2.5,
            lon_20_25E = 2.5,
            lon_15_20E = 2.5,
            lon_10_15E = 2.5,
            lon_5_10E = 2.5,
            lon_0_5E = 2.5,
        )
    #Testing index page
    def test_indexview(self):
        client = Client()
        response = client.get('/')
        #testing if the status_code, template used and content of the response are correct.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global_temp/index.html')
        self.assertContains(response, 'The Global Historical Climatology Network (GHCN) is an integrated database of climate that summaries from land surface stations across the globe')
    #Testing temp_details page
    def test_tempdetailsview(self):
        client = Client()
        #passing the year and month values as POST request.
        response = client.post('/temp/details/', {'year':'2002', 'monthID': '1'})
        #testing if the status_code, template used and content of the response are correct.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global_temp/temperature_details.html')
        self.assertContains(response, 'Missing values are represented by the value -9999')

    #Testing the map page
    def test_mapview(self):
        client = Client()
        #sending parameter to the map page
        response = client.get('/temp/map/2001/1')
        #testing if the status_code, template used and content of the response are correct.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global_temp/map.html')
        self.assertContains(response, 'OpenStreetMap')
    
    #Testing the chart page
    def test_chartview(self):
        client = Client()
        response = client.get('/temp/charts/')
        #testing if the status_code, template used and content of the response are correct.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'global_temp/charts.html')
        self.assertContains(response, 'Click on change chart type buttom to change the chart from bar to line and vicevers')
    
    #Testing the values in the response of map_details page
    def test_map_view(self):
        url = reverse('map_detail', args=[2002, 2])
        response = self.client.get(url)
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # Check if the content matches the expected output
        # You can use response.content or response.context to check the returned content
        # For example, if you expect the lat and lon_165_170W values in the response:
        self.assertIn(b'55.3781', response.content)
        self.assertIn(b'-3.4360', response.content)