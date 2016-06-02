from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from ....models import User, Good, Request, Supply

#Adds an offer to the Database
def add_offer(request):
    new_goodtype = request.POST.get('optgood', None)
    new_quantity = request.POST.get('unit',None)
    new_location = request.POST.get('location', None)
    new_range = request.POST.get('area', None)

    allowed_goods = {'water', 'food', 'woundcare' , 'clothes' , 'accomodation'}
    try:
        int(new_quantity)
    except (ValueError, TypeError):
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Anzahl an.",
        })
    try:
        int(new_location)
    except (ValueError, TypeError):
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Postleitzahl an.",
        })
    try:
        int(new_range)
    except (ValueError, TypeError):
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Reichweite an.",
        })


    if new_goodtype not in allowed_goods :
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte wählen sie eine Güterkategorie aus.",
        })
    if int(new_quantity) < 1:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Anzahl an.",
        })
    if len(str(new_location)) != 5:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Postleitzahl an.",
        })
    if int(new_range) < 1:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Bitte geben sie eine gültige Reichweite an.",
        })

    category = Good.objects.get(pk=new_goodtype)
    user = User.objects.get(pk='Bob')

    new_request = Supply(username = user, goodName = category, quantity = new_quantity, postalCode = new_location)
    Request.create(new_request)

    return HttpResponseRedirect(reverse('tim_app:ranking'))

#Adds a request to the Database
def add_request(request):
    new_goodtype = request.POST.get('optgood', None)
    new_desc = request.POST.get('other', None)
    new_quantity = request.POST.get('unit',None)
    new_location = request.POST.get('location', None)
    new_prio = request.POST.get('prio', None)

    allowed_goods = {'water', 'food', 'woundcare' , 'clothes' , 'accomodation', 'other'}
    try:
        int(new_quantity)
    except (ValueError, TypeError):
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte geben sie eine gültige Anzahl an.",
        })
    try:
        int(new_location)
    except (ValueError, TypeError):
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte geben sie eine gültige Postleitzahl an.",
        })
    try:
        int(new_prio)
    except (ValueError, TypeError):
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte wählen sie eine Priorität aus.",
        })


    if new_goodtype not in allowed_goods:
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte wählen sie eine Güterkategorie aus.",
        })
    print(new_desc)
    print(new_goodtype)
    if (new_goodtype == 'other' and (new_desc == None or len(new_desc) == 0)) or (new_goodtype != 'other' and new_desc != None and len(new_desc) != 0):
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte geben sie eine Beschreibung ihrer Anfrage ein",
    })
    if int(new_quantity) < 1:
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte geben sie eine gültige Anzahl an.",
        })
    if len(str(new_location)) != 5:
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte geben sie eine gültige Postleitzahl an.",
        })
    if (int(new_prio) != 1) and (int(new_prio) != 2) and (int(new_prio) != 3):
        return render(request, 'tim_app/request.html', {
            'error_message': "Bitte wählen sie eine Priorität aus.",
        })
    category = Good.objects.get(pk=new_goodtype)
    user = User.objects.get(pk='Bob')
    if new_goodtype == 'other':
        misc = new_desc
    else:
        misc = 'NULL'

    new_request = Request(username = user, goodName = category, misc = misc, quantity = new_quantity, priority = new_prio, postalCode = new_location)
    Request.create(new_request)
    return HttpResponseRedirect(reverse('tim_app:ranking'))
