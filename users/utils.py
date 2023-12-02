import os
from twilio.rest import Client

account_sid = 'AC17f9d4feb4c400975b0b92362204004a'
auth_token = 'ef92168767dce2c709fca9a59ec54d23'

def send_SMS(verification_code , phone_number):
    client = Client(account_sid, auth_token)
    # send sms
    message = client.messages.create(
        body=f"Hi, your verification code to LovejoyAntique app is {verification_code}",
        from_='+17655363031',
        to='+254758262427'
    )
    
    return message
