from requests import get
url = 'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages'
char = 97
page_count={}
while char<=122:
    latter = chr(char)
    new_url= f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{latter}/pages'
    response = get(new_url)
    data = response.json().get('page_count')
    page_count[latter]=data
    char+=1
print(page_count)