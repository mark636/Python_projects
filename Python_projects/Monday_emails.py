import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open(r"C:\Users\marko\Python_projects\Python_projects\Python_projects\quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    print(quote)
    my_email = "markous007@gmail.com"
    password = "axhhhezwdrksgtrs"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Monday Motivation \n\n" + quote)
        connection.close()



