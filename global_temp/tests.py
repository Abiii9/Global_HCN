# global_temp/tests.py

from django.test import TestCase
from django.urls import reverse

from .models import Year, Temperature

class GlobalTempViewTests(TestCase):
    
    def setUp(self):
        Year.objects.get_or_create(id=2020, year=2020)

        Temperature.objects.create(
            year_id=2020,
            latitude=-23.5,
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
            # Add other required fields with valid values
        )
    
    def test_temperature_view(self):
        url = reverse('map_detail', args=[2020, 2])
        response = self.client.get(url)

        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the content matches the expected output
        # You can use response.content or response.context to check the returned content
        # For example, if you expect the lat and lon_165_170W values in the response:
        self.assertIn(b'57.149651', response.content)
        self.assertIn(b'-2.099075', response.content)
