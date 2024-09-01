import requests
url = 'https://www.itshikkha.com//wp-json/wp/v2/users'
response = requests.get(url)
data = response.json()
for user in data:
    user_name = user.get('name')
    print(user_name)