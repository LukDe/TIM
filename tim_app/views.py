from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .static.tim_app.python import offer_request as ofre


def login(request):
    return render(request, 'tim_app/login.html')


def offer(request):
    if request.method == 'POST':
        return ofre.add_offer(request)
    else:
        return render(request, 'tim_app/offer.html')


def request(request):
    if request.method == 'POST':
        return ofre.add_request(request)
    else:
        return render(request, 'tim_app/request.html')


def list(request):
	return render(request, 'tim_app/list.html')

