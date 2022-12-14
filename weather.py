import requests

API_KEY = '07526094ce283e8c5687d4c0938ba362'  # Fetches data from weather.org
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY = input('Enter name of the city: ') # Enter name of any city you would like to find

request_url = f"{BASE_URL}?appid={API_KEY}&q={CITY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    day_temp = data['main']['temp']
    temperature = 1.8*(day_temp-273)+32
    print('The temperature is',round(temperature), 'f') # Returns temperature in degrees Fahrenheit
    weather = data['weather'][0]['description']
    print('Expect ',weather) # Returns expected weather condition eg expect Rain
else:
    print('An error occured') #Returns error if its unable to fetch the data






