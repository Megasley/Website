from endpoints.get_token import token
import requests

url = "https://topups.reloadly.com/accounts/balance"

headers = {
	"Accept": "application/com.reloadly.topups-v1+json",
	"Authorization": f"Bearer {token}"
}

balance_response = requests.get(url, headers=headers).json()
print(f"Current balance: {balance_response['balance']} {balance_response['currencyCode']}")