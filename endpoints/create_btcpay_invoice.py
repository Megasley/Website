import requests
from keys import api_key, store_id
def create_invoice(amount, currency):
  url = f'https://btcpay0.voltageapp.io/api/v1/stores/{store_id}/invoices'

  amount = (float(amount) + (0.02*float(amount)))

  header = {
      'Authorization' : f'token {api_key}',
      'Content type' : 'application/json',
  }
  parameters = {
    "checkout": {
      "speedPolicy": "HighSpeed",
      "expirationMinutes": 90,
      "redirectURL": "http://127.0.0.1:5000/success",
      "redirectAutomatically": True,
    },
    "receipt": {
      "enabled": False,
      # "showQR": None,
      # "showPayments": None
    },
    "amount": str(amount),
    "currency": currency,
  }

  invoice_response = requests.post(url=url, headers=header, json=parameters).json()
  checkout_invoice_link = invoice_response['checkoutLink']
  return checkout_invoice_link

print(create_invoice(amount='500', currency='NGN'))