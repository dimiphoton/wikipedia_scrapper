import requests
import json
print('import done')

response = requests.get('https://country-leaders.onrender.com/countries')
data=response.json()

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)
