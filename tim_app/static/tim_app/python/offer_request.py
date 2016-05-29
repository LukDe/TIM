from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from dateutil.parser import parse

def add_offer(request):
    new_goodtype = request.POST.get('optgood', None)
    new_quantity = request.POST.get('unit',None)
    new_location = request.POST.get('location', None)
    new_range = request.POST.get('area', None)

    allowed_goods = {'water', 'food', 'woundcare' , 'clothes' , 'accomodation'}
    try:
        int(new_quantity)
    except ValueError:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please specify a valid quantity.",
        })
    try:
        int(new_location)
    except ValueError:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please enter a valid Zip Code.",
        })
    try:
        int(new_range)
    except ValueError:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please specify a valid range in which you will be able to deliver the goods.",
        })


    if new_goodtype not in allowed_goods :
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please select a goods category.",
        })
    if int(new_quantity) < 1:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please specify a valid quantity.",
        })
    if len(str(new_location)) != 5:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please enter a valid Zip Code.",
        })
    if int(new_range) < 1:
        return render(request, 'tim_app/offer.html', {
            'error_message': "Please specify a valid range in which you will be able to deliver the goods.",
        })
    return HttpResponseRedirect(reverse('tim_app:login'))

def add_request(request):
    new_goodtype = request.POST.get('optgood', None)
    new_desc = request.POST.get('other', None)
    new_quantity = request.POST.get('unit',None)
    new_location = request.POST.get('location', None)
    new_prio = request.POST.get('prio', None)

    allowed_goods = {'water', 'food', 'woundcare' , 'clothes' , 'accomodation', 'other'}
    try:
        int(new_quantity)
    except ValueError:
        return render(request, 'tim_app/request.html', {
            'error_message': "Please specify a valid quantity.",
        })
    try:
        int(new_location)
    except ValueError:
        return render(request, 'tim_app/req.html', {
            'error_message': "Please enter a valid Zip Code.",
        })
    try:
        int(new_prio)
    except ValueError:
        return render(request, 'tim_app/request.html', {
            'error_message': "Please select a priority.",
        })


    if new_goodtype not in allowed_goods:
        return render(request, 'tim_app/request.html', {
            'error_message': "Please select a goods category.",
        })
    if (new_goodtype == 'other' and new_desc == None) or (new_goodtype != 'other' and new_desc != None):
        return render(request, 'tim_app/request.html', {
            'error_message': "Please enter a description of what you are requesting.",
    })
    if int(new_quantity) < 1:
        return render(request, 'tim_app/request.html', {
            'error_message': "Please specify a valid quantity.",
        })
    if len(str(new_location)) != 5:
        return render(request, 'tim_app/request.html', {
            'error_message': "Please enter a valid Zip Code.",
        })
    if (int(new_prio) != 12) and (int(new_prio) != 24) and (int(new_prio) != 36):
        return render(request, 'tim_app/request.html', {
            'error_message': "Please select a priority.",
        })

    return HttpResponseRedirect(reverse('tim_app:login'))
