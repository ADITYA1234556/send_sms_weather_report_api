import os
import requests
from twilio.rest import Client
API_KEY= "SECURE"
account_sid = 'SECURE'
auth_token = 'SECURE'
LATITUDE = 51.509865
LONGITUDE = -0.118092
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 6
}
response = requests.get(url = ENDPOINT, params= parameters )
response.raise_for_status()
data = response.json()
print (len(data["list"]))
print(data["list"][0]["dt_txt"])
required_data = (data["list"][3]["weather"][0]["id"])
TIME = []
will_rain = False
for i in range(len(data["list"]) - 1):
    condition = data["list"][i]["weather"][0]["id"]
    time = data["list"][i]["dt_txt"]
    if condition < 700:
        will_rain = True
        TIME.append(time)
    else:
        print("good")
if will_rain:
    print(TIME)
    client = Client(account_sid, auth_token)
    message = client.messages.create(body = f"It will rain at {TIME} carry your umbrella", from_= '+447883317242', to= '+447587997662')
    print(message.status)
