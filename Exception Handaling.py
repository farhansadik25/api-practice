import requests

urls = ['https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages/1',
'https://discovery-api.npollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages/2',
'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages/3',
'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages/4']

for url in urls:
    try:
        print(requests.get(url).status_code)
    except:
        continue