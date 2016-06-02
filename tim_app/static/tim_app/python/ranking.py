from ....models import User, Good, Request, Supply

#Creates a context for ranking.html that includes all misc. requests and the total request amounts of standard goods
def get_context():
    misc_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "other"))
    water_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "water"))
    food_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "food"))
    clothes_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "clothes"))
    woundcare_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "woundcare"))
    accomodation_requests = Request.objects.all().filter(goodName = Good.objects.get(pk = "accomodation"))

    total_water = 0
    total_food = 0
    total_clothes = 0
    total_woundcare = 0
    total_accomodation = 0

    for request in water_requests:
        total_water = total_water + request.quantity

    for request in food_requests:
        total_food = total_food + request.quantity

    for request in clothes_requests:
        total_clothes = total_clothes + request.quantity

    for request in woundcare_requests:
        total_woundcare = total_woundcare + request.quantity

    for request in accomodation_requests:
        total_accomodation = total_accomodation + request.quantity

    context = {'request_list': misc_requests, 'total_water': total_water, 'total_food': total_food, 'total_clothes':total_clothes, 'total_woundcare':total_woundcare,'total_accomodation': total_accomodation}
    return context