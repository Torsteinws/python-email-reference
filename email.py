import os
from typing import List
from dotenv import load_dotenv
from string import Template
import re

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
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    emails = get_mail_list()
    template = read_template('./message.txt')

    for mail in emails:
        name = re.split('@', mail)[0] # use regex to get the part of the mail address before '@'
        message = template.substitute(PERSON_NAME=name)
        print(message)
        print('--------------------------------------------')


if __name__ == "__main__":
    os.system('cls')
    send_email()