import os
import requests
from twilio.rest import Client

"""dictionary to add parameters for the OpenWeatherMap api"""
parameters = {
    "lat": 3.118576,
    "lon": 101.663008,
    "exclude": "current,minutely,daily",
    "appid": "2c39e16fa9a79c6352a8d3a737314ead"
}

"""Variables to run the Twilio options to send SMS"""
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

"""Get the data from API"""
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

"""Get the id which has the weather condition"""
condition = False
weather_id = data["hourly"][:12]
for item in weather_id:
    condition_code = int(item["weather"][0]["id"])
    if condition_code < 600:
        condition = True

"""Send SMS if the condition is true!"""
if condition:
    message = client.messages.create(
        body="Bring un umbrella, it will rain soon, be careful and have a nice day!",
        from_='+15017122661',
        to='+15558675310'
    )

    print(message.sid)
