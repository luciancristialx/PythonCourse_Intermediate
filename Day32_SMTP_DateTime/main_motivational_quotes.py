import datetime as dt
import random
import smtplib

EMAIL = "email_address"
EMAIL_APP_PWD = "gmail_app_pwd"

now = dt.datetime.now()
current_week_day = now.weekday()
def get_random_quote():
    with open('quotes.txt','r') as my_file:
        quotes = my_file.read()
        quotes_list = quotes.split("\n")

    return random.choice(quotes_list)

def send_email(**kwargs):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # Secure connection
        connection.ehlo()
        connection.starttls()
        connection.login(user = EMAIL, password = EMAIL_APP_PWD)

        header = 'To:' + 'recipient_email_address' + '\n' + 'From:' + EMAIL + '\n' + 'subject:Motivational Quote\n'
        content = header + kwargs['emailBody']

        # Send email
        connection.sendmail(EMAIL, 'recipient_email_address', content)

if current_week_day == 6:
    random_quote = get_random_quote()
    send_email(emailBody = random_quote)