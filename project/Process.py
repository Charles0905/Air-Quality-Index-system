import json
import matplotlib.pyplot as plt
#coding:utf-8
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


# Acquire the data from city_aqi.json which we get in the main.py
filename = './dataFile/city_aqi.json'
with open(filename, 'r') as f_obj:
    json_data = json.load(f_obj)


# Get the AQI(air quality index) of every city. Make the city_name to be the key and the aqi value to be the value
city_aqi = {}
for item in json_data:
    city_aqi[item['city_name']] = item['city_AQI']


# Sort from small to large for city_aqi
# Remove the city with aqi equals 0 because Some monitoring points did not upload data
sorted_city_aqi = sorted(city_aqi.items(), key=lambda item:item[1])
city_aqi_without0 = []
for item in sorted_city_aqi:
    if int(item[1]) != 0:
        city_aqi_without0.append(item)


# Get the top ten cities with the best AQI (lower is better) and ten cities with the worst AQI
# The number of cities in the list may be greater than 10 because some cities are tied for tenth same time
reverse_city_aqi_without0 = city_aqi_without0[::-1]

def get10cites(before, after):
    for city in before:
        if len(after) < 10:
            after.append(city)
        else:
            if city[1] == after[-1][1]:
                after.append(city)
            else:
                break
    return after

best_aqi_cites = get10cites(city_aqi_without0,[])
worst_aqi_cites =get10cites(reverse_city_aqi_without0,[])


# Draw a scatter plot and save to local
def draw(cities_list,title_name):
    cities_list_name = []
    cities_list_aqi = []
    for item in cities_list:
        cities_list_name.append(item[0])
        cities_list_aqi.append(item[1])

    plt.title(title_name)
    plt.xlabel('Cities')
    plt.ylabel('AQI value')
    plt.scatter(cities_list_name, cities_list_aqi, s=40, c='red', marker='o')

    for a, b in zip(cities_list_name, cities_list_aqi):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

    plt.savefig(title_name, dpi=300)
    plt.show()

draw(best_aqi_cites,'Top 10 cities with the best AQI')
draw(worst_aqi_cites,'10 cities with the worst AQI')
