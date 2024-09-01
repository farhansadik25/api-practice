import requests
url = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'
res = requests.get(url)
if res.status_code == 200:
    data = res.json().get('meals')
    meal_list = []
    for datas in data:
        meal_name = datas.get('strMeal')
        meal_list.append(meal_name)
print(meal_list)