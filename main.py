import pandas
import smtplib
import datetime as dt
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
print(data)

My_EMAIL = "python.gmtest@gmail.com"
PASSWORD = "japk vivn hvwk munx"

now = dt.datetime.now()
for address in data.iterrows():
    month = address[1]["month"]
    day = address[1]["day"]
    name = address[1]["name"]
    email = address[1]["email"]
    if month == now.month and day == now.day:
        letter_no = random.randint(1,3)
        with open(f"letter_templates/letter_{letter_no}.txt", "r") as f:
            letter_cover = f.read()
        result_cover = letter_cover.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=My_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=My_EMAIL, to_addrs=email, msg=f"subject: Happy Birthday\n\n{result_cover}")







# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

