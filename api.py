import requests

my_city = 'boston'
api_key = 'f16a3084be77a020f9139a17538ae497'

api_call = f'http://api.openweathermap.org/data/2.5/weather?q={my_city}&appid={api_key}'

weather_data = requests.get(api_call).json()['main']

print(weather_data['temp'])
print(weather_data['pressure'])
print(weather_data['humidity'])

my_weather = 'temp is ' + str(weather_data['temp']) +' pressure ' + str(weather_data['pressure']) + " Humidity is " + str(weather_data['humidity'])
print(my_weather)
# f16a3084be77a020f9139a17538ae497

# api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}