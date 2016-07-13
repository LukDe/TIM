from tim_app.models import User, Good, Request, Supply
from math import radians, cos, sin, asin, sqrt
from sms.utils import send_sms_message
import copy
from datetime import timedelta

#matches with one or more supply objects if possible, returns true on success 
def find_match_for_request(rid):
    request = Request.objects.get(id = rid)

    #get all active objects from category
    s_list = Supply.objects.filter(active = True, goodName = request.goodName)

    #filter matches in radius and create a list
    supply_list = []
    for s in s_list:
        if (distance(s.location, request.location) <= (request.radius + s.radius)):
            supply_list.append(s)
	
    #if no possible matches in radius found, terminate and return false
    if len(supply_list) == 0 :
        return False
		
    # check for exact quantity matches
    exact_matches = list(filter(lambda s: s.quantity == request.quantity,  supply_list))

    # if exact matches exist, choose closest one & return
    if len(exact_matches) > 0:
        exact_matches = sorted(exact_matches, key=lambda supply: distance(supply.location, request.location))
        # exact match found, send sms
        print("match complete")
        match(request, exact_matches[0])
        #deactivate request and offer
        Request.objects.filter(id = rid).update(active = False)
        Supply.objects.filter(id = exact_matches[0].id).update(active = False)
        #request.active = False #
        #exact_matches[0].active = False #
        return True
		
    # if no exact matches exist, prefer smallest one with quantity > that of the request
    if len(exact_matches) == 0:
        #good_matches = sorted(supply_list.filter(lambda x : x.quantity > request.quantity), key=lambda supply: (supply.quantity, distance(supply.location, request.location)))
        good_matches = [x for x in supply_list if x.quantity > request.quantity]
        good_matches = sorted(supply_list, key=lambda supply: (supply.quantity, distance(supply.location, request.location)))		
		# if no good matches(ones that satisfy the request) exist, find one that satisfies a part of it
        if not good_matches:
            #sort offers and take the biggest one
            #other_matches = sorted(supply_list.filter(lambda x : x.quantity < request.quantity), key=lambda supply: (-supply.quantity, distance(supply.location, request.location)))
            other_matches = [x for x in supply_list if x.quantity < request.quantity]
            other_matches = sorted(supply_list, key=lambda supply: (-supply.quantity, distance(supply.location, request.location)))
            print("match incomplete")
            match_incomplete(request, other_matches[0])

            #deactivate request and offer
            Request.objects.filter(id = rid).update(active = False)
            Supply.objects.filter(id = other_matches[0].id).update(active = False)            
			
	       # create inactive remainder entry (with different primary key) 
            remainder = copy.deepcopy(Request.objects.get(id = rid))
            remainder.quantity = request.quantity - other_matches[0].quantity
            remainder.active = False
            remainder.pk = None
            remainder.save()
            return True
			
        #choose the smallest offer that satisfies request
        match_incomplete(request, good_matches[0])
        print("match incomplete")
        #deactivate request and offer
        Request.objects.filter(id = rid).update(active = False)
        Supply.objects.filter(id = good_matches[0].id).update(active = False) 
        return True



# matches with one or more request objects if possible, returns true on success
def find_match_for_supply(sid):
    supply = Supply.objects.get(id = sid)

    # get all active objects
    r_list = Request.objects.filter(active = True, goodName = supply.goodName)

    # get all in range ((where distance between request and offer <= (request's radius + offer's radius)) and create a list
	
    request_list = []
    for r in r_list:
        if (distance(r.location, supply.location) <= (supply.radius + r.radius)):
            request_list.append(r)
    if len(request_list) == 0:
        return False

        # check for exact quantity matches
    exact_matches = list(filter(lambda r: r.quantity == supply.quantity,  request_list))

    # if exact matches exist, choose by remaining time
    if len(exact_matches) > 0:
        exact_matches = sorted(exact_matches,
                               key = lambda request: (request.creationDate + timedelta(days = request.priority),
                                                     distance(r.location, supply.location)))
        #exact match found
        match(exact_matches[0], supply)
        print("match complete")		
        #deactivate request and offer
        Supply.objects.filter(id = sid).update(active = False)
        Request.objects.filter(id = exact_matches[0].id).update(active = False)
        #exact_matches[0].active = False
        #supply.active = False
        return True
    
    # if no exact matches exist, prefer biggest one with quantity < that of the offer
    if len(exact_matches) == 0:
        good_matches = list(filter(lambda r: r.quantity < supply.quantity,  request_list))
        if len(good_matches) == 0:
            # no smaller matches, choose the smallest from the bigger requests
            other_matches = list(filter(lambda r: r.quantity > supply.quantity,  request_list))
            other_matches_sorted = sorted(other_matches, key=lambda request: (request.quantity, distance(request.location, supply.location)))

            match_incomplete(other_matches[0], supply)
            print("match incomplete")			
            #deactivate request and offer
            Supply.objects.filter(id = sid).update(active = False)
            Request.objects.filter(id = other_matches_sorted[0].id).update(active = False)			

			# create inactive remainder entry from request (with different primary key) 
            remainder = copy.deepcopy(Request.objects.get(id = other_matches_sorted[0].id))
            remainder.quantity = other_matches_sorted[0].quantity - supply.quantity
            remainder.pk = None
            remainder.active = False
            remainder.save()
            return True

		#smaller request exists, match with the biggest from the smaller requests
        good_matches_sorted = sorted(good_matches, key = lambda request:( (supply.quantity - request.quantity), distance(request.location, supply.location))) # same as above
        match_incomplete(good_matches_sorted[0], supply)
        print("match incomplete")
        #deactivate request and offer
        Supply.objects.filter(id = sid).update(active = False)
        Request.objects.filter(id = good_matches_sorted[0].id).update(active = False)
        return True



#exact match: message both parties
def match(r, s):
    # retrieve users
    requesting_person = User.objects.get(username = r.username)
    offering_person = User.objects.get(username = s.username)
    unit = Good.objects.get(goodName = r.goodName).unit
    #messaging the requesting person
    send_sms_message(requesting_person.phoneNr, "Match mit " + offering_person.phoneNr + " : " + str(s.quantity) + " " + str(unit) + " " + s.goodName.goodName)
    #messaging the offering person
    send_sms_message(offering_person.phoneNr, "Match mit " + requesting_person.phoneNr + " : " + str(r.quantity) + " " + str(unit) + " " + r.goodName.goodName)


	
#incomplete match: send two sms messages and an extra about remainder
def match_incomplete(r, s):
    #quantity of match
    quantity = min(r.quantity, s.quantity)
    #retrieve users for phone numbers
    requesting_person = User.objects.get(username = r.username)
    offering_person = User.objects.get(username = s.username)
    #determining unit of goods
    unit = Good.objects.get(goodName = r.goodName).unit

    #messaging the requesting person
    send_sms_message(requesting_person.phoneNr, "Match mit " + offering_person.phoneNr + " : " + str(quantity) + " " + str(unit) + " " + s.goodName.goodName)
    #messaging the offering person
    send_sms_message(offering_person.phoneNr, "Match mit " + requesting_person.phoneNr + " : " + str(quantity) + " " + str(unit) + " " + r.goodName.goodName)
	
	#find out if request or offer is bigger, send an extra message to the user whose offer/request is not completely exhausted
    if (r.quantity > s.quantity):
        send_sms_message(requesting_person.phoneNr, "Wir konnten nur " + str((quantity / r.quantity)*100) + "%" " deiner Anfrage erfüllen. Die Restanfrage kannst du auf der Webseite aktivieren.")
    else:
        send_sms_message(offering_person.phoneNr, "Wir konnten nur " + str((quantity / s.quantity)*100) + "%" " deines Angebots ausschöpfen. Erstelle ein neues Angebot, falls du den Rest noch anbieten möchtest.")
		
		
def distance(location1, location2):
    #calculate distance between request and offer and return the value
    # split string (in format "longitude,latitude")
    location_1 = location1.split(",")
    location_2 =  location2.split(",")
    lon1 = float(location_1[0])
    lat1 = float(location_1[1])
    lon2 = float(location_2[0])
    lat2 = float(location_2[1])
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km