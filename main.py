import smtplib

# Set up SMTP server and prompt the user to enter his sign in info

smtp_server = 'smtp.office365.com'
smtp_port = 587
username = str(input('Please enter your Outlook email address: '))
password = str(input('Please enter your password: '))

# prompt the user to enter mail content and recipient address
author_add = username
recipient_add = str(input("Please enter the recipient's email address: ")).lower()
subject = str(input('Please enter a subject for the email: '))
body = str(input('Please enter the body of the email: '))

# create a header for the email
head = f"From: {author_add}\r\nTo: {recipient_add}\r\nSubject: {subject}\r\n"

# try to connect to the SMTP server, log in and send the mail
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        message = head + '\r\n' + body
        server.sendmail(author_add, recipient_add, message)
        print('email was sent successfully!')
except smtplib.SMTPException as error:
    print(f'An error has occurred: {error}')