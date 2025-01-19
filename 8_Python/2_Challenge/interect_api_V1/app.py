import requests

APP_ID = "db77ab55f455406daab087ce77f0f881"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()["rates"]

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["GBP"]

print(f"USD {usd_amount} is GBP {gbp_amount}")