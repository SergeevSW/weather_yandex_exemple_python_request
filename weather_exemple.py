import requests

# key from https://developer.tech.yandex.ru/keys/
TOKEN = 'your_key'

url = 'https://api.weather.yandex.ru/v1/forecast?lat=55.75396&lon=37.620393'
head = {'content-type': 'application/json',
        'X-Yandex-API-Key': TOKEN}

r = requests.get(url, headers=head)
print(r.json())
