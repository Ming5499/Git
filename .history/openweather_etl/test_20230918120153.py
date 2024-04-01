import time
import json
from kafka import KafkaProducer
import requests


# kafka_booststrap_servers = ''
# kafka_topic_name = ''

# producer = KafkaProducer(boostrap_servers=kafka_booststrap_servers,
#                          value_serializer = lambda v: json.dumps(v).encode('utf-8'))


city_name = "hanoi"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="

full_url = 'https://api.openweathermap.org/data/2.5/weather?q=danang&appid=fce40c3ad84e88aba9f09388dc5ca04e'



def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius




def etl_weather_data(full_url):
    

    r = requests.get(full_url)
    #Get data
    data = r.json()


    city_name = data["name"]
    temp_celsius = kelvin_to_celsius(data["main"]["temp"])
    humidity = data["main"]["humidity"]
    
    json_message = {'CityName': city_name,'Temperature': temp_celsius,'Humidity': humidity, 'CreatOnTime': time.strftime("%Y-%m-%d %H:%M:%S")}
    return json_message

etl_weather_data(full_url)

    