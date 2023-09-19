from twilio.rest import Client
from os import environ

# Environment variables
ACCOUNT_SID = environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = environ.get("TWILIO_AUTH_TOKEN")
MESSAGE_SID = environ.get("TWILIO_MESSAGING_SERVICE_SID")


# Twilio client
class SMS:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_message(self, otp, to):
        body = f'Your OTP is {otp} for Wool Project'
        message = self.client.messages.create(body=body, messaging_service_sid=MESSAGE_SID, to=to)

        print(message.sid)
        return message.sid

if __name__ == '__main__':
    sms = SMS()
    sms.send_message(123456, '+919302627594')