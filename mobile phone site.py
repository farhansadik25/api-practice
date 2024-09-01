import requests
import base64
import json

wp_user = 'farhan'
wp_pass = 'WOG2 bsrz CkYU O1h5 7Jbc 9KMy'
wp_credemtial = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credemtial.encode())
wp_headers = {'Authorization':f'Basic {wp_token.decode("utf-8")}'}


def slugify(text):
    return text.strip().replace(' ','-')

def paragraph(text):
    return f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'

def heading_two(text):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'

def table(text):
    table_codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key,value in text.items():
        tr_codes = f'<tr><td>{key}</td><td>{value}</td></tr>'
        table_codes += tr_codes
    table_codes += '</tbody></table></figure><!-- /wp:table -->'
    return table_codes

def media_photo(photo_url,alter_teg):
    return f'<!-- wp:image {{"sizeSlug":"large","align":"center"}} --><figure class="wp-block-image aligncenter size-large"><img src="{photo_url}" alt="{alter_teg}"/></figure><!-- /wp:image -->'


json_url = 'https://mobile-phone-server.vercel.app/phones'
phones = requests.get(json_url).json().get('RECORDS')

for phone in phones:

    phone_name = phone.get('name')
    picture = phone.get('picture')
    specifications_str = phone.get('specifications')
    specifications = json.loads(specifications_str)
    released_at = phone.get('released_at')
    chipset = phone.get('chipset')


    title = f'{phone_name} Price In Bangladesh'
    paragraph_body = f'{phone_name} has been relesed on {released_at}. It\'s comes with {chipset} chipset. You can buy it.'

    first_heading_two = f'{phone_name} Full Specifications'
    first_dictionary = {
        'Name' : phone_name,
        'Release Date' : released_at,
        'chipset' : chipset
    }

    post_image = media_photo(picture,phone_name)
    post_paragraph = paragraph(paragraph_body)
    post_table_one = table(first_dictionary)
    post_heading_two = heading_two(first_heading_two)
    post_table_two = table(specifications)

    wp_post_content = post_paragraph + post_image + post_table_one + post_heading_two + post_table_two

    post_data = {
        'title' : title.title(),
        'content' : wp_post_content,
        'slug' : slugify(title),
        'status':'publish',
        'categories' : '2'
    }

    url_endpoint= 'https://localhost/python/wp-json/wp/v2/posts'
    res = requests.post(url_endpoint,headers=wp_headers,json=post_data,verify=False)