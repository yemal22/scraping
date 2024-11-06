import requests
from bs4 import BeautifulSoup
# send email
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder
email_content = ""

# extra 