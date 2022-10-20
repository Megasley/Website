import requests
from endpoints.get_token import token
from endpoints.get_operator_by_phone import get_operator

def get_data_operator(number, country_iso):
	operator_name = f"{get_operator(number=number, country_iso=country_iso)['name']} Data"

	url = "https://topups.reloadly.com/operators/countries/NG?includeData=true"

	headers = {
		"Accept": "application/com.reloadly.topups-v1+json",
		"Authorization": f"Bearer {token}"
	}

	data_response = requests.get(url, headers=headers).json()
	for operator in data_response:
		if operator["name"] == operator_name:
			return operator

print(get_data_operator(number='07083245678', country_iso='NG'))