from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .static.tim_app.python import offer_request as ofre

from .static.tim_app.python import ranking as rank
from .models import *


def login(request):
    return render(request, 'tim_app/login.html')


def ranking(request):
    context = rank.get_context()
    return render(request, 'tim_app/ranking.html', context)


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

def impressum(request):
    return render(request, 'tim_app/impressum.html')

def user(request):
	return render(request, 'tim_app/user.html')
