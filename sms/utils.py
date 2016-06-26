from django.conf import settings

import twilio
from twilio.rest import TwilioRestClient

def send_sms_message(to_number, body):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    return client.messages.create(
        body = body,
        to = to_number,
        from_ = settings.TWILIO_PHONE_NUMBER,
    )
