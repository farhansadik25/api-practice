import requests
email = input("Enter your email: ")
url = f"https://api.mailcheck.ai/email/{email}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json().get('disposable')
    if not data:
        print("You can login")
    else:
        print("You can not login with disposable email.")
