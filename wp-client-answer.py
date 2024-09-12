import os
from twilio.rest import Client
from dotenv import load_dotenv 
import sqlite3
from time import sleep

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
my_wp_number= os.getenv('MY_WP_NUMBER')

if not account_sid or not auth_token or not twilio_number:
    raise ValueError("Environment variables were not loaded correctly.")

client = Client(account_sid, auth_token)

conn = sqlite3.connect('responses.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS saved_contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT NOT NULL
    )
''')
conn.commit()

def send_message(phone, message):
    try:
        client.messages.create(
            from_=twilio_number,
            body=message,
            to=f'whatsapp:{phone}',
        )
    except Exception as e:
        print(f"Error sending message to {phone}: {e}")

def save_contact(phone):
    try:
        cursor.execute('INSERT INTO saved_contacts (phone) VALUES (?)', (phone,))
        conn.commit()
    except Exception as e:
        print(f"Error saving contact {phone}: {e}")

phones = [my_wp_number, '+5511995522666']
initial_message = "Would you like to participate in our promotion? Reply with Yes or No."

for phone in phones:
    send_message(phone, initial_message)
    print(f"Message sent to {phone}")
    
    answer = input(f"Simulation: Did the user {phone} respond Yes or No? ")

    if answer.lower() == 'yes':
        save_contact(phone)
        print(f"Contact {phone} saved to the database.")
    elif answer.lower() == 'no':
        print(f"Message cycle ended for {phone}.")
    
    sleep(1)

cursor.close() 
conn.close()   
