import os
from typing import List
from dotenv import load_dotenv


def get_mail_list() -> List[str]:
    emails = [] 

    with open('mailing-list.txt', 'r') as file:
        for line in file:
            email = line.strip()
            emails.append(email)

    return emails

def send_email():
    
    load_dotenv()
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    emails = get_mail_list()
    print(emails)

if __name__ == "__main__":
    os.system('cls')
    send_email()