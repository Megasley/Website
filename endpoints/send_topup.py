import requests
from endpoints.get_token import token

def send_topup(amount, operator_id, number, country_code):
	url = "https://topups.reloadly.com/topups"

	payload = {
		"operatorId": operator_id,
		"amount": amount,
		"useLocalAmount": True,
		"recipientPhone": {
			"countryCode": country_code,
			"number": number}
	}
	headers = {
		"Content-Type": "application/json",
		"Accept": "application/com.reloadly.topups-v1+json",
		"Authorization": f"Bearer {token}"
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.status_code