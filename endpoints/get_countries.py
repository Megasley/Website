import requests
from endpoints.get_token import token

url = "https://topups.reloadly.com/countries"

headers = {
	"Accept": "application/com.reloadly.topups-v1+json",
	"Authorization": f"Bearer {token}"
}

countries_response = requests.get(url, headers=headers).json()
# count = 0
# for country in countries_response:
# 	count += 1
# 	print(country['currencyCode'])
# print(countries_response[0])



