import smtplib
import ssl
import requests
import pandas
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

url = "https://api.weather.gov/gridpoints/MTR/91,108/forecast/hourly"

r = requests.get(url)
res = r.text

email_sender = "justinweatherapp@gmail.com"
email_password = os.getenv('EMAIL_PASS')
# email_receiver = "lgreenbaum1214@gmail.com"
email_receiver = "justinjagoss@gmail.com"

subject = "Test of weather app"
body = res

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as gmail_router:
    gmail_router.login(email_sender, email_password)
    gmail_router.sendmail(email_sender, email_receiver, em.as_string())