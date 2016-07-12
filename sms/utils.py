from django.conf import settings

import twilio
from twilio.rest import TwilioRestClient

def send_sms_message(to_number, body):
    client = TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )
    return client.messages.create(
        body = body,
        to = to_number,
        from_ = settings.TWILIO_PHONE_NUMBER,
    )

def parse_sms_request(request):
    """
    Parses a string received as sms from the user. The function assumes
    a format of `request/offer,goodName,quantity`. If the message is not on the
    correct format, returns a dictionary with an error key,
    otherwise a dictionary with keys: `type, goodName, quantity`
    """
    def error(msg):
        return {
            'error': msg,
        }

    formatted_req = list(map(lambda x: x.strip(), request.split(',')))
    # The message expects three arguments.
    if (len(formatted_req) != 3):
        return error('Expected format: (offer/request),goodName,quantity')

    if (formatted_req[0] != 'offer' and formatted_req[0] != 'request'):
        return error('Expected format: (offer/request),goodName,quantity')

    return {
        'type': formatted_req[0],
        'goodName': formatted_req[1],
        'quantity': formatted_req[2],
    }



