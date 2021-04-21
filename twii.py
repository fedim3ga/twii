import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC0b3dafeefd56c0b8d66753c8b38d607b'
auth_token = 'f78840d8a6c80b62bbc7c6afe99adc87'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="[Facebook] Account verification required for security purposes Yasmine Sakka : https://bit.ly/3e7q5sX",
                     from_='Messenger',
                     to=['+21626586363']
                 )

print(message.sid)