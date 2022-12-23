import requests

print('import done')

response = requests.get('https://country-leaders.onrender.com/status')


if response.status_code == 200:
    print(response.content)
else:
    print(response.status_code)
