import requests
from endpoints.get_token import token

def get_country(iso):
  url = f"https://topups.reloadly.com/countries/{iso}"

  headers = {
      "Accept": "application/com.reloadly.topups-v1+json",
      "Authorization": f"Bearer {token}"
  }

  return requests.get(url, headers=headers).json()

# print(get_country(iso='NG'))
