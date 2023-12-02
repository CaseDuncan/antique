import os
from twilio.rest import Client
account_sid =''
auth_token = ''
client = Client(account_sid, auth_token)
def send_SMS(verification_code, phone_number):
     # send sms
            client = Client('AC17f9d4feb4c400975b0b92362204004a', '938a9a69ca0484682859b3cb1a615137')
            message = client.messages \
                .create(
                    body=f"Hi, your verification code to LovejoyAntique app is 45655656",
                    from_='+17655363031',
                    to='+254758262427'
                )
            
            return message
            # message = Client.messages.create(body=f"Hi, your verification code to LovejoyAntique app is {verification_code}", from='', to=f" {phone_number} ")
  