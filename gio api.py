import requests
ip_api ="https://api.ipify.org?format=json"
response = requests.get(ip_api)
ip = response.json().get('ip')
gio_api = f"http://ip-api.com/json/{ip}"
response_new = requests.get(gio_api)
gio_data = response_new.json()
country = gio_data.get('country')


print(f'My country name is {country}.')