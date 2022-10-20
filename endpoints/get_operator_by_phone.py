import requests
from endpoints.get_token import token
def get_operator(number, country_iso):
	phone = number
	country_iso_code = country_iso

	url = f"https://topups.reloadly.com/operators/auto-detect/phone/{phone}/countries/{country_iso_code}?suggestedAmountsMap=true&suggestedAmounts=true"

	headers = {
		"Accept": "application/com.reloadly.topups-v1+json",
		"Authorization": f"Bearer {token}"
	}



	return requests.get(url, headers=headers).json()

# print(get_operator(number="07082142747", country_iso='NG'))