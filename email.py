import os
from dotenv import load_dotenv

def send_email():
    print('Sending email...')

    load_dotenv()
    username = os.getenv('EMAIL_USERNAME')
    password = os.getenv('EMAIL_PASSWORD')

    print(username, password)

if __name__ == "__main__":
    os.system('cls')
    send_email()