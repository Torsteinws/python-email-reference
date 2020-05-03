import os
from typing import List
from dotenv import load_dotenv
from string import Template
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get every line in .txt file, and return them as a list of strings
def get_mail_list() -> List[str]:
    emails = [] 

    with open('mailing-list.txt', 'r') as file:
        for line in file:
            email = line.strip()
            emails.append(email)

    return emails

# Read a .txt file as a template string
def read_template(path :str):
    with open(path, 'r') as file:
        return Template(file.read())

def send_email():

    load_dotenv()

    emails = get_mail_list()
    template = read_template('./message.txt')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        # Get credentials from .env file
        username = os.getenv('EMAIL_USERNAME')
        password = os.getenv('EMAIL_PASSWORD')

        # Login to email account
        server.ehlo()
        server.login(username, password)

        for email_address in emails:
            name = re.split('@', email_address)[0] # use regex to get the part of the mail address before '@'
            message = template.substitute(PERSON_NAME=name)

            # Todo: experiment with the mime types
            msg = MIMEMultipart()       # Mail
            msg['From'] = username      # From this email user
            msg['To'] = email_address   # To this address
            msg['Subject'] = 'Hello World'  # With this tile 
            msg.attach(MIMEText(message))   # With this text body

            server.send_message(msg)

if __name__ == "__main__":
    os.system('cls')
    send_email()