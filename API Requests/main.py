import requests
import datetime as dt

MY_LAT = 24.8607
MY_LONG = 67.0011
TIME = 0
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# #print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude,latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": TIME
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]

print(sunrise)
print(sunset)

now = dt.datetime.now()
time_now = now.hour
print(time_now)
