from libs.openexchange import OpenExchangeClient
import requests
import time

APP_ID = "db77ab55f455406daab087ce77f0f881"

client = OpenExchangeClient(app_id=APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)


print(f"USD {usd_amount} is GBP {gbp_amount}")