import json
import matplotlib.pyplot as plt


# Acquire the data from city_aqi.json which we get in the main.py
filename = './dataFile/city_aqi.json'
with open(filename, 'r') as f_obj:
    json_data = json.load(f_obj)


# Get the AQI(air quality index) of every city.
# Make various parameters to be the key and the aqi value to be the value
pm25_aqi = {}
co_aqi = {}
mo2_aqi = {}
pm10_aqi = {}
o3_aqi = {}
so2_aqi = {}
for item in json_data:
    pm25_aqi[item['city_PM2.5']] = item['city_AQI']
    co_aqi[item['city_CO']] = item['city_AQI']
    mo2_aqi[item['city_MO2']] = item['city_AQI']
    pm10_aqi[item['city_PM10']] = item['city_AQI']
    o3_aqi[item['city_O3']] = item['city_AQI']
    so2_aqi[item['city_SO2']] = item['city_AQI']


# Make each dictionary remove 0 and arrange it in order
def sortfuc(aqi):
    sorted_city_aqi = sorted(aqi.items(), key=lambda item:item[1])
    city_aqi_without0 = []
    for item in sorted_city_aqi:
        if int(item[1]) != 0:
            city_aqi_without0.append(item)
    return city_aqi_without0

pm25_aqi = sortfuc(pm25_aqi)
co_aqi = sortfuc(co_aqi)
mo2_aqi = sortfuc(mo2_aqi)
pm10_aqi = sortfuc(pm10_aqi)
o3_aqi = sortfuc(o3_aqi)
so2_aqi = sortfuc(so2_aqi)


# Draw a scatter plot and save to local
def draw(parament_aqi, title_name, xlabl, color):
    cities_list_parament = []
    cities_list_aqi = []
    for item in parament_aqi:
        cities_list_parament.append(item[0])
        cities_list_aqi.append(item[1])

    plt.title(title_name)
    plt.xlabel(xlabl)
    plt.ylabel('AQI value')
    plt.scatter(cities_list_parament, cities_list_aqi, s=10, c=color, marker='o')

    plt.savefig(title_name, dpi=300)
    plt.show()

draw(pm25_aqi, 'pm25_aqi', 'pm25 value', 'b')
draw(co_aqi, 'co_aqi', 'co value', 'g')
draw(mo2_aqi, 'mo2_aqi', 'mo2 value', 'c')
draw(pm10_aqi, 'pm10_aqi', 'pm10 value', 'm')
draw(o3_aqi, 'o3_aqi', 'o3 value', 'y')
draw(so2_aqi, 'so2_aqi', 'so2 value', 'k')