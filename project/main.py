import requests
from bs4 import BeautifulSoup
import json


def get_soup_obj(url):
    url_obj = requests.get(url)
    soup = BeautifulSoup(url_obj.content, 'html.parser')
    return soup


def get_secondpage(city_aqi_item):
    """
    Function:
         Get some index of the city through the secondary website
    return value:
         Get the city's various indices through the city's corresponding link (secondary URL)
    """
    bs = get_soup_obj(city_aqi_item)
    data_div_tag = bs.find('div', class_='span12 data')
    value_data_div_list = data_div_tag.find_all('div', class_='value')

    city_other_data = []
    for i in range(8):
        city_other_data.append(float(value_data_div_list[i].text))

    return city_other_data


def get_fistpage_and_secondpage(url, soup):
    """
    Function:
         Get the city name and corresponding link (secondary URL) through the primary URL, and then get some index of
         the city through the corresponding link (secondary URL).
     parameter:
         Url: primary URL
         Soup: source code data for the primary URL that needs to be analyzed
     return value:
         Returns a list whose elements are dictionaries. The elements of the dictionary are the name of the city, the
         link to the city, and the various indices of the city.
    """
    city_aqi_list = []

    bottom_div = soup.find('div', class_='all')
    city_tag_list = bottom_div.find_all('li')

    for city_tag in city_tag_list:
        city_aqi = {}
        city_aqi['city_name'] = city_tag.find('a').text
        city_link = 'http://www.pm25.in' + city_tag.find('a')['href']
        city_aqi['city_link'] = city_link
        city_other_data = get_secondpage(city_link)
        city_aqi['city_AQI'] = city_other_data[0]
        city_aqi['city_PM2.5'] = city_other_data[1]
        city_aqi['city_PM10'] = city_other_data[2]
        city_aqi['city_CO'] = city_other_data[3]
        city_aqi['city_MO2'] = city_other_data[4]
        city_aqi['city_O3'] = city_other_data[5]
        city_aqi['city_03_8h'] = city_other_data[6]
        city_aqi['city_SO2'] = city_other_data[7]

        city_aqi_list.append(city_aqi)

    return city_aqi_list


# Save the city_aqi_data to city_aqi.json
def write_city_aqi(city_aqi_data):
    file_path = './dataFile/city_aqi.json'


    with open (file_path , 'w')  as f_obj:
        json.dump(city_aqi_data,f_obj)

# Running module
if __name__ == "__main__":

    url = 'http://www.pm25.in/'
    soup = get_soup_obj(url)
    city_aqi_list = get_fistpage_and_secondpage(url, soup)
    write_city_aqi(city_aqi_list)

    # Browse the data we get
    print(city_aqi_list)

