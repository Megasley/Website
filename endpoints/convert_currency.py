import requests

def convert_to_usd(amount, currency):
	url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

	querystring = {"from":currency,"to":"USD","amount":amount}

	headers = {
		"X-RapidAPI-Key": "8876e6ea2fmsh92a7925c34db6f8p1d89f3jsnf4c9996e8dbe",
		"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring).json()
	amount = response['result']['convertedAmount']
	return amount

# print(convert_to_usd(amount=100, currency='NGN'))