# GHCN Limited

## What is the application about?
This application was developed by a team of five as a part of coursework at the University of Aberdeen. This application helps you to visualize the  temperature recorded across the globe from year 2000 to 2014. The data can be viewed in tabular form, geographical map view and graph form. The Model-View-Template architecture pattern has been followed. The database used in this application is SQLite3. Leaflet and chart.js packages have been used to perform data visualization.

## Information regarding the data.
The Global Historical Climatology Network (GHCN) is an integrated database of climate that summaries from land surface stations across the globe. This data set contains gridded mean temperature anomalies, or departures from a reference value or long-term average, from the Global Historical Climatology Network-Monthly (GHCN-M) version 3.2.1 temperature data set.  
The gridded anomalies were produced from GHCN-M bias corrected data. Each month of data consists of 2,592 gridded data points produced on a 5° by 5° basis for the entire globe (72 longitude by 36 latitude grid boxes).

* Frequency: Monthly  
* Period: 2000 to 2014  

The data are formatted by year, month, latitude and longitude. There are 72 longitude grid values per line -- each grid is labeled as a concatenation of "lon", "w" or "e", then the degree. The latitude is captured in the "lat" field where the value indicates the lower bound of a grid cell (e.g. 85 indicates 85-90N whereas -90 indicates 85-90S). Longitude values are written from 180°W to 180°E, and latitude values from 90°N to 90°S.

## Features

GHCN web application offers you the following features to visualize the data.
* Table feature under the visualize option helps you to view the data in tabular form.
* Map view feature in the table view page helps you to plot the same data points  in a global map view. 
* Charts feature under the visualize option helps you to check the variation over the years of a point on globle.
* You can also compare the temperature variations between two different points by using the charts compare feature.

## Requirements

All the packages and libraries required for this application to run can be found in requirements.txt file.

## Installation

To install the application, you need to clone/download the application  

```bash
git clone "repo_link"
```
Run the below command to install pyenv

```bash
pyenv install 3.10.7 # to install the pyenv on your server.
```

You need to create a virtual environment. Set present location in termial to root directory of the project and then run the following commands to create and start the virtunal environment.  
```bash
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```

To install the dependencies run the following command.
```bash
pip install -r requirements.txt
```




## Deployment

To start the application run the following command from root directory.
```bash
 python3 manage.py runserver
```
To terminate the application use ctrl+c or follow the commands shown in terminal.



## Demo

The application is deployed and you can find it using the below link:
[GHCN Limited](https://global-hcn.onrender.com/)

## Credits
The data source for this application was taken from https://www.kaggle.com/datasets/noaa/global-historical-climatology-network. 
It contains a detailed table values of temperature from years 1995 to 2018 across the globe.
We used open source (chart.js) https://www.chartjs.org/ to implement chart view of the data and (leaflet) https://leafletjs.com/ to implement geographical map view.