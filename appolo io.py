import requests
import csv

pages = {}
json_url = 'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages'
latters = 'abcd'
for latter in latters:
    page_url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{latter}/pages'
    response = requests.get(page_url).json().get('page_count')
    pages[latter] = response



with open('url.txt','w+') as file:
    for page_latter,total_page in pages.items():
        for page_number in range(1,total_page+1):
            json_company_url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{page_latter}/pages/{page_number}'
            file.write(json_company_url + '\n')


# with open('url.txt','r') as data_file:
#     url_list = data_file.readlines()

# with open('company.txt','w+',encoding='utf-8') as file:
#     for url in url_list:
#         url_data = requests.get(url.strip()).json()
#         for company in url_data:
#             company_id = company.get('id')
#             company_url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/entity/{company_id}'
#             file.writelines(company_url+'\n')


# with open('company.txt','r',encoding='utf-8') as file:
#     company_url = file.readlines()


# with open('company_data.csv', 'a+', newline='',encoding='utf-8') as csvfile:
#     fieldnames = ['company_name', 'company_logo_url','location']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for end_points in company_url:
#         company_data = {}
#         res = requests.get(end_points.strip()).json()
#         company_data['company_name'] = res.get('name')
#         company_data['company_logo_url'] = res.get('logo_url')
#         location_city = res.get('location').get('city')
#         location_state = res.get('location').get('state')
#         location_country = res.get('location').get('country')
#         company_data['location'] = f'{location_city}, {location_state}, {location_country}'
#         writer.writerow(company_data)