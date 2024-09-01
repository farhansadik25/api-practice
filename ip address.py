import requests
url="https://api.ipify.org?format=json"
print(requests.get(url).json().get('ip'))
respons = requests.get(url)
data = respons.json()

ip = data["ip"]

print(ip)

print(respons.json().get("ip"))
