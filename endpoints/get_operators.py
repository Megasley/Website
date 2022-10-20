import requests
from endpoints.get_token import token
url = "https://topups.reloadly.com/operators?includeBundles=true&includeData=true&suggestedAmountsMap=true"

headers = {
	"Accept": "application/com.reloadly.topups-v1+json",
	"Authorization": f"Bearer {token}"
}

operators_response = requests.get(url, headers=headers).json()
# print(operators_response)
