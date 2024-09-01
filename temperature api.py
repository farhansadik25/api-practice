import requests
city_name = input("Enter the city name: ")
x=city_name.title()
api_key = "adbf30fde8cc911f5d0f0f19c01d8357"
main_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(main_url)
data = response.json().get('main')
temp = response.json().get('main').get('temp')
feels_like = response.json().get('main').get('feels_like')
temp_min = response.json().get('main').get('temp_min')
temp_max = response.json().get('main').get('temp_max')
print(f'City name is {x}. Today temperature is {temp}. Feels like {feels_like}. Minimum temperature is {temp_min} and Maximum temperature is {temp_max}.')
