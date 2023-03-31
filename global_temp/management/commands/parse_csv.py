import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from global_temp.models import Year, Temperature


# We use the command tools so that we gain access to our models and database connections
# https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        Year.objects.all().delete()
        Temperature.objects.all().delete()

        print("table dropped successfully")
        # create table again
        for x in range(2000,2015):
            year_obj = Year.objects.create(
                year=x
            )
            year_obj.save()
        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(
                str(base_dir) + '/global_temp/data_set/data.csv',
                newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line

            # parsing each row and inserting the values in appropriate model attribute.
            for row in reader:
                print(row)
                year = int(row[0])
                year_obj = Year.objects.filter(year=year).first()
                temperature = Temperature.objects.create(
                    year=year_obj,
                    month=int(row[1]),
                    latitude=row[2],
                    lon_175_180W=int(row[3]),
                    lon_170_175W = int(row[4]),
                    lon_165_170W = int(row[5]),
                    lon_160_165W = int(row[6]),
                    lon_155_160W = int(row[7]),
                    lon_150_155W = int(row[8]),
                    lon_145_150W = int(row[9]),
                    lon_140_145W = int(row[10]),
                    lon_135_140W = int(row[11]),
                    lon_130_135W = int(row[12]),
                    lon_125_130W = int(row[13]),
                    lon_120_125W = int(row[14]),
                    lon_115_120W = int(row[15]),
                    lon_110_115W = int(row[16]),
                    lon_105_110W = int(row[17]),
                    lon_100_105W = int(row[18]),
                    lon_95_100W = int(row[19]),
                    lon_90_95W = int(row[20]),
                    lon_85_90W = int(row[21]),
                    lon_80_85W = int(row[22]),
                    lon_75_80W = int(row[23]),
                    lon_70_75W = int(row[24]),
                    lon_65_70W = int(row[25]),
                    lon_60_65W = int(row[26]),
                    lon_55_60W = int(row[27]),
                    lon_50_55W = int(row[28]),
                    lon_45_50W = int(row[29]),
                    lon_40_45W = int(row[30]),
                    lon_35_40W = int(row[31]),
                    lon_30_35W = int(row[32]),
                    lon_25_30W = int(row[33]),
                    lon_20_25W = int(row[34]),
                    lon_15_20W = int(row[35]),
                    lon_10_15W = int(row[36]),
                    lon_5_10W = int(row[37]),
                    lon_0_5W = int(row[38]),
                    lon_175_180E=int(row[74]),
                    lon_170_175E = int(row[73]),
                    lon_165_170E = int(row[72]),
                    lon_160_165E = int(row[71]),
                    lon_155_160E = int(row[70]),
                    lon_150_155E = int(row[69]),
                    lon_145_150E = int(row[68]),
                    lon_140_145E = int(row[67]),
                    lon_135_140E = int(row[66]),
                    lon_130_135E = int(row[65]),
                    lon_125_130E = int(row[64]),
                    lon_120_125E = int(row[63]),
                    lon_115_120E = int(row[62]),
                    lon_110_115E = int(row[61]),
                    lon_105_110E = int(row[60]),
                    lon_100_105E = int(row[59]),
                    lon_95_100E = int(row[58]),
                    lon_90_95E = int(row[57]),
                    lon_85_90E = int(row[56]),
                    lon_80_85E = int(row[55]),
                    lon_75_80E = int(row[54]),
                    lon_70_75E = int(row[53]),
                    lon_65_70E = int(row[52]),
                    lon_60_65E = int(row[51]),
                    lon_55_60E = int(row[50]),
                    lon_50_55E = int(row[49]),
                    lon_45_50E = int(row[48]),
                    lon_40_45E = int(row[47]),
                    lon_35_40E = int(row[46]),
                    lon_30_35E = int(row[45]),
                    lon_25_30E = int(row[44]),
                    lon_20_25E = int(row[43]),
                    lon_15_20E = int(row[42]),
                    lon_10_15E = int(row[41]),
                    lon_5_10E = int(row[40]),
                    lon_0_5E = int(row[39]),
                )
                temperature.save() # saving the object in the database.

        print("data parsed successfully")


