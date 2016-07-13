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
    correct format, returns `None`, otherwise a dictionary, with keys as:
       type, goodName, quantity, radius, priority
    """
    error_msg = False
    requestType = 0
    requestGood = 0
    requestQuantity = 1
    requestRadius = 1
    requestPriority = 1
    requestMisc = 0

    formatted_req = list(map(lambda x: x.strip(), request.split(',')))

    if (len(formatted_req) == 0):
        error_msg = ('Erwartetes Format: offer/request,"Warenname","Anzahl", "Radius", "Priorität"')
    elif (formatted_req[0] == 'offer'):
        if (len(formatted_req) != 4):
            error_msg = ('Erwartetes Format: offer,"Warenname","Anzahl", "Radius"')
        else:
            requestType = formatted_req[0]
            requestGood = formatted_req[1]
            requestQuantity = formatted_req[2]
            requestRadius = formatted_req[3]
    elif (formatted_req[0] == 'request'):
        if (len(formatted_req) != 5):
            error_msg = ('Erwartetes Format: request,"Warenname","Anzahl"/"Beschreibung", "Radius", "Priorität"')
        elif ((int(formatted_req[4]) != 1) and (int(formatted_req[4]) != 2) and (int(formatted_req[4]) != 3)):
            error_msg = ('Erwartetes Format: request,"Warenname","Anzahl", "Radius", "Priorität"; Priorität muss 1,2 oder 3 sein. ' + formatted_req[4])
        else:
            requestType = formatted_req[0]
            requestGood = formatted_req[1]
            requestRadius = formatted_req[3]
            requestPriority = formatted_req[4]
            if (formatted_req[1] == 'other'):
                requestMisc = formatted_req[2]
            else:
                requestQuantity = formatted_req[2]
    return {
        'type': requestType,
        'goodName': requestGood,
        'quantity': requestQuantity,
        'radius': requestRadius,
        'priority': requestPriority,
        'misc': requestMisc,
        'error': error_msg
    }



