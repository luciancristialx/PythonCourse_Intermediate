import smtplib

my_email = "email_address"
my_pwd = "gmail_app_pwd"
# Connect to SMTP email server
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # Secure connection
    connection.ehlo()
    connection.starttls()
    connection.login(user = my_email, password = my_pwd)

    header = 'To:' + 'recipient_email_address' + '\n' + 'From:' + my_email + '\n' + 'subject:email_subject\n'
    content = header + 'Hello'

    # Send email
    connection.sendmail(my_email, 'recipient_email_address', content)
