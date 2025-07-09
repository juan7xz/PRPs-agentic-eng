from twilio.rest import Client
import os

class TwilioService:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def make_call(self, to_number, from_number, twiml_url):
        call = self.client.calls.create(
            to=to_number,
            from_=from_number,
            url=twiml_url
        )
        return call.sid

    def send_sms(self, to_number, from_number, message):
        message = self.client.messages.create(
            to=to_number,
            from_=from_number,
            body=message
        )
        return message.sid
