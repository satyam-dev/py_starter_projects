from twilio.rest import Client
import config


client = Client(config.twilio_account_sid, config.twilio_auth_token)

message = client.messages.create(
    to="+919999999999",
    from_='+15097403131',
    body="Yay! Hello from Python!")

print(message.sid)
