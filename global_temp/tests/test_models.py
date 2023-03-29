from django.test import Client, TestCase
from global_temp.models import Year, Temperature

class TempModelTest(TestCase):
    @classmethod
    #setting up the data for the Year and Temperature Models.
    def setUpTestData(cls):
        Year.objects.create(year = 2001)
        Year.objects.create(year = 2002)
        year_obj1 = Year.objects.get(id=1)
        year_obj2 = Year.objects.get(id=2)
        Temperature.objects.create(
            year = year_obj1,
            month = 3,
            latitude= '45-50N',
            lon_175_180W = 35,
            lon_170_175W = 3,
            lon_165_170W = -5,
            lon_160_165W = -50,
            lon_155_160W = -33,
            lon_150_155W = 23,
            lon_145_150W = 45,
            lon_140_145W = 13,
            lon_135_140W = 23,
            lon_130_135W = -67,
            lon_125_130W = -50,
            lon_120_125W = 21,
            lon_115_120W = -3,
            lon_110_115W = -17,
            lon_105_110W = -13,
            lon_100_105W = -45,
            lon_95_100W = 23,
            lon_90_95W = 37,
            lon_85_90W = 5,
            lon_80_85W = 6,
            lon_75_80W = -7,
            lon_70_75W = -8,
            lon_65_70W = -9,
            lon_60_65W = 11,
            lon_55_60W = 15,
            lon_50_55W = -15,
            lon_45_50W = 21,
            lon_40_45W = 23,
            lon_35_40W = 10,
            lon_30_35W = 9,
            lon_25_30W = 8,
            lon_20_25W = 45,
            lon_15_20W = 57,
            lon_10_15W = 13,
            lon_5_10W = 56,
            lon_0_5W = 13,
            lon_175_180E = -9,
            lon_170_175E = -13,
            lon_165_170E = -15,
            lon_160_165E = -90,
            lon_155_160E = -67,
            lon_150_155E = 101,
            lon_145_150E = 151,
            lon_140_145E = 131,
            lon_135_140E = 15,
            lon_130_135E = -89,
            lon_125_130E = 13,
            lon_120_125E = -17,
            lon_115_120E = -91,
            lon_110_115E = -101,
            lon_105_110E = -131,
            lon_100_105E = -121,
            lon_95_100E = -91,
            lon_90_95E = -133,
            lon_85_90E = 33,
            lon_80_85E = 23,
            lon_75_80E = 9,
            lon_70_75E = 7,
            lon_65_70E = 6,
            lon_60_65E = 5,
            lon_55_60E = 4,
            lon_50_55E = 3,
            lon_45_50E = 2,
            lon_40_45E = 1,
            lon_35_40E = -9999,
            lon_30_35E = 235,
            lon_25_30E = 65,
            lon_20_25E = 35,
            lon_15_20E = -31,
            lon_10_15E = -21,
            lon_5_10E = -91,
            lon_0_5E = 21,
        )
        Temperature.objects.create(
            year = year_obj2,
            month = 3,
            latitude= '45-50N',
            lon_175_180W = 3,
            lon_170_175W = 31,
            lon_165_170W = -5,
            lon_160_165W = -5,
            lon_155_160W = -3,
            lon_150_155W = 2,
            lon_145_150W = 45,
            lon_140_145W = 13,
            lon_135_140W = 23,
            lon_130_135W = -6,
            lon_125_130W = -50,
            lon_120_125W = 21,
            lon_115_120W = -33,
            lon_110_115W = -17,
            lon_105_110W = -13,
            lon_100_105W = -45,
            lon_95_100W = 23,
            lon_90_95W = 31,
            lon_85_90W = 5,
            lon_80_85W = 6,
            lon_75_80W = -7,
            lon_70_75W = -8,
            lon_65_70W = -9,
            lon_60_65W = 11,
            lon_55_60W = 17,
            lon_50_55W = -154,
            lon_45_50W = 2,
            lon_40_45W = 23,
            lon_35_40W = 11,
            lon_30_35W = 9,
            lon_25_30W = 8,
            lon_20_25W = 45,
            lon_15_20W = 58,
            lon_10_15W = 11,
            lon_5_10W = 5,
            lon_0_5W = 1,
            lon_175_180E = -91,
            lon_170_175E = -1,
            lon_165_170E = -17,
            lon_160_165E = -9,
            lon_155_160E = -6,
            lon_150_155E = 10,
            lon_145_150E = 121,
            lon_140_145E = 111,
            lon_135_140E = 17,
            lon_130_135E = -8,
            lon_125_130E = 7,
            lon_120_125E = -7,
            lon_115_120E = -91,
            lon_110_115E = -10,
            lon_105_110E = -15,
            lon_100_105E = -13,
            lon_95_100E = -9,
            lon_90_95E = -11,
            lon_85_90E = 37,
            lon_80_85E = 29,
            lon_75_80E = 91,
            lon_70_75E = 71,
            lon_65_70E = 63,
            lon_60_65E = 51,
            lon_55_60E = 41,
            lon_50_55E = 39,
            lon_45_50E = 23,
            lon_40_45E = 13,
            lon_35_40E = -67,
            lon_30_35E = -81,
            lon_25_30E = 65,
            lon_20_25E = 36,
            lon_15_20E = -30,
            lon_10_15E = -23,
            lon_5_10E = -90,
            lon_0_5E = 23,
        )
    #Testing the Year model
    def test_year(self):
        year = Year.objects.get(id=1)
        self.assertEqual(year.year,2001)
    #Testing the Temperature model
    def test_temperature(self):
        temp1 = Temperature.objects.get(id=1)
        temp2 = Temperature.objects.get(id=2)
        self.assertEqual(temp1.lon_0_5E,21)
        self.assertEqual(temp2.year.id,2)
    #Testing the str method of the Year model.
    def test_strmethod(self):
        year = Year.objects.get(id=1)
        self.assertEqual(str(year.year), '2001')
