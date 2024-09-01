import requests
import base64
json_url = 'https://jsonplaceholder.typicode.com/posts'
posts = requests.get(json_url).json()
wp_user = 'farhan'
wp_pass = 'WOG2 bsrz CkYU O1h5 7Jbc 9KMy'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization':f'Basic {wp_token.decode('utf-8')}'}

def slug(text):
    slug_text = text.strip().replace(' ','-')
    return slug_text


for post in posts:
    url_endpoint = 'https://localhost/python/wp-json/wp/v2/posts'
    data = {
        'title': post['title'],
        'content': post['body'],
        'slug':slug(post['title']),
        'status':'publish'
    }
    response = requests.post(url_endpoint,json=data,headers=wp_headers,verify=False)