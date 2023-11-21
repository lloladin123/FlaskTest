import requests

param = {"param1": "value1", "param2": 'value2'}
url = "http://localhost:5000/get_data"

response = requests.get(url, params=param)
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)