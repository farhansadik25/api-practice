import base64
import requests
wp_user = 'farhan'
wp_pass = 'WOG2 bsrz CkYU O1h5 7Jbc 9KMy'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization':f'Basic {wp_token.decode('utf-8')}'}
url_endpoint = 'https://localhost/python/wp-json/wp/v2/posts'
data = {
    'title':'This is title',
    'content':'The content for the post.',
    'slug':'this-is-slag',
    'status':'publish'
}
response = requests.post(url_endpoint,headers=wp_headers,json=data,verify=False)
print(response)