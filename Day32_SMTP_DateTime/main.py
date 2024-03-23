import smtplib

my_email = "test@gmail.com"
my_pwd = "test"
# Connect to SMTP email server
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    # Secure connection
    connection.ehlo()
    connection.starttls()
    connection.login(user = my_email, password = my_pwd)

    header = 'To:' + 'test1@yahoo.com' + '\n' + 'From:' + my_email + '\n' + 'subject:testmail\n'
    content = header + 'Hello'

    # Send email
    connection.sendmail(my_email, 'test1@yahoo.com', content)
