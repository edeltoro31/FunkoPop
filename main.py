import requests

response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")

code = response.status_code
print(code)

if code == 200:
    print(response.json())
