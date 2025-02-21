import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 14.599512
MY_LONG = 120.984222
MY_EMAIL = "" #ADD YOUR EMAIL
MY_PASSWORD = "" #ADD YOUR EMAIL APP PASSWORD


def iss_overhead():

    # ------ ISS Position API

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)

    print(f"ISS is in: {iss_position}")
    print(f"You are in: ({MY_LONG}, {MY_LAT})")

    if MY_LONG-5 <= iss_longitude <= MY_LONG+5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        return True
    else:
        return False


def is_dark():

    # ------ Sunrise and Sunset API

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    data = sunset_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise >= time_now >= sunset:
        return True


if iss_overhead() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:International Space Station!\n\nLook up!"
        )
else:
    print("ISS too far")
