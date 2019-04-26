Obtain the Air Quality Index of cities in China online and conduct a simple data analysis
=======

### Introduction
This is my first python individual project | Author: Chenhui Yang | Course: EE551B

### Purposals
Use the `requests` module and the `BeautifulSoup` module in `bs4` to analyze the China Air Quality Index Testing website whose URL is  http://www.pm25.in/ and obtain the daily air quality data of every city. Download the data to local and do some simple data analyze to them

### Architecture
* main.py <br>
The main.py is used to get the air quality data from the China AQI testing website <br>
Module: `requests`, `BeutifulSoup` in the `bs4`, `json` (`Scrapy` can also be used in there) <br>
Function: Dowmload various parameters of every city and save them into city_aqi.json. The parameters include the city_name, AQI(air quality index), PM2.5, PM10, CO, MO2, O3, O3/8h, SO2 <br>

* Process.py <br>
The process.py is used to get the best air quality cites and the worst cites <br>
Module: `json`, `matplotlib.pyplot` <br>
Function: Filter the data in city_aqi.json and acquire the scatters of top 10 cites with the best air quality that day and 10 cites with the worst air quality city in China <br>

* Simple DA.py <br>
The process.py is used to analyze simply the relation between diffrent parameters and AQI <br>
Module: `json`, `matplotlib.pyplot` <br>
Function: Filter the data in city_aqi.json and acquire the scatters of PM2.5-AQI, CO-AQI, MO2-AQI, PM10-AQI, 03-AQI, SO2-AQI. According to those scatters we can make some rough inferences about which the parameters would affect AQI. <br>

* Scatters <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/Top_10_cities_with_the_best_AQI.png) <br>
The scatter of Top 10 Chinese cities with the best air quality Index on 04/24/2019 <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/10_cities_with_the_worst_AQI.png) <br>
The scatter of Top 10 Chinese cities with the worst air quality Index on 04/24/2019 <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/pm25_aqi.png) <br>
The scatter with pm2.5-aqi <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/co_aqi.png) <br>
The scatter with co-aqi <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/mo2_aqi.png) <br>
The scatter with mo2-aqi <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/pm10_aqi.png) <br>
The scatter with pm10-aqi <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/o3_aqi.png) <br>
The scatter with o3-aqi <br>
![](https://github.com/yangchenhui9509/myEE551project/raw/master/project/scatter/so2_aqi.png) <br>
The scatter with so2-aqi <br>

* Conclusion <br>
From those scatters, we can get the conclusion that AQI is positively correlated with PM2.5 value and PM10 value and The correlation between AQI and CO, MO2, 03, SO2 is not very obvious <br>

### Todo
* Get those data online daily for a month and analyze every city average air quality parameters <br>
* Learn how to use `pandas` to analyze data

### Author
Chenhui Yang

### License
