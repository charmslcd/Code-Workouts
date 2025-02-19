import smtplib
import pandas as pd
import datetime as dt
import random

MY_EMAIL = "<YOUR EMAIL>>" #input a gmail email, if not a gmail email, change the SMTP in the code below
MY_PASSWORD = "<YOUR EMAIL PASSWORD>" #the app password generated for the email address

data = pd.read_csv("birthdays.csv")

data_dict = data.to_dict("records")
print(data_dict)


current_date = dt.datetime.now()

for birthday in data_dict:
    birthdate = dt.date(year=birthday["year"], month=birthday["month"], day=birthday["day"])

    if birthdate.month == current_date.month and birthdate.day == current_date.day:
        letter_choice = random.randint(1, 3)
        if letter_choice == 1:
            with open("letter_templates/letter_1.txt", "r") as file:
                msg = file.read()
        elif letter_choice == 2:
            with open("letter_templates/letter_2.txt", "r") as file:
                msg = file.read()
        else:
            with open("letter_templates/letter_3.txt", "r") as file:
                msg = file.read()

        update_msg = msg.replace("[NAME]", birthday["name"])
        print(f"{birthday["email"]}")
        print(update_msg)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject:Happy Birthday!\n\n{update_msg}"
            )


