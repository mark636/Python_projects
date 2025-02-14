import requests
from datetime import datetime
import smtplib
import time
import os

MY_EMAIL = os.getenv("markous007@gmail.com")
MY_PASSWORD = os.getenv("axhhhezwdrksgtrs")
MY_LAT = -33.733020675032 
MY_LONG = 150.93973057088868

def is_iss_overhead():
    try:
        response = requests.get(url="http://api.wheretheiss.at/v1/satellites/25544", timeout=10)
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["latitude"])
        iss_longitude = float(data["longitude"])

        # Your position is within +5 or -5 degrees of the ISS position.
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True
    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        time_now = datetime.utcnow().hour

        if time_now >= sunset or time_now <= sunrise:
            return True
    except requests.RequestException as e:
        print(f"Error fetching sunrise/sunset data: {e}")
        return False

while True:
    if is_iss_overhead() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject:Look Up\n\nThe ISS is above you in the sky."
                )
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
    time.sleep(60)


