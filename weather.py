
import requests

API_KEY = '07526094ce283e8c5687d4c0938ba362'
BASE_URL = 'https://openweathermap.org/data/2.5/weather'
DULUTH = 'duluth'
LONG = -92.105507
LAT = 46.782841

request_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LONG}&exclude=&appid={API_KEY}'

response = requests.get(request_url)

if response.status_code == 200:
    print('SUCCESS')
else :
    print('not succesful')

