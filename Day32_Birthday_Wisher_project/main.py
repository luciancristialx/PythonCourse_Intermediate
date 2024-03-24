import random
import pandas as pd
import datetime as dt
import smtplib

EMAIL = "email_address"
EMAIL_APP_PWD = "gmail_app_pwd"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - Completed

# 2. Check if today matches a birthday in the birthdays.csv

df_birthdays = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
current_day = now.day
current_month = now.month

filtered_df = df_birthdays[(df_birthdays['month']==current_month) & (df_birthdays['day']==current_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if filtered_df.empty:
    print("No Birthday wish to be sent today!")
else:
    name = filtered_df["name"][0]
    random_int = random.randint(1,3)
    with open(f"./letter_templates/letter_{random_int}.txt","r") as letter_template:
        email_body = letter_template.read()
        email_body = email_body.replace("[NAME]",name)

# 4. Send the letter generated in step 3 to that person's email address.

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # Secure connection
    connection.ehlo()
    connection.starttls()
    connection.login(user = EMAIL, password = EMAIL_APP_PWD)

    header = 'To:' + 'recipient_email_address' + '\n' + 'From:' + EMAIL + '\n' + 'subject:Happy Birthday!\n'
    content = header + email_body

    # Send email
    connection.sendmail(EMAIL, 'recipient_email_address', content)




