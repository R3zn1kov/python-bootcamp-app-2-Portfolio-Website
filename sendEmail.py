import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "l.dilillo99@gmail.com"
    password = os.getenv("PASSWORDPYTHONPROJECT2")
    receiver = "l.dilillo99@gmail.com"
    context = ssl.create_default_context()
    # Create secure SSL context
    context = ssl.create_default_context()
    # Try to log in to server and send email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
