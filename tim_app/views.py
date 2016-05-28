from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .static.tim_app.python import offer_request as ofre 

# Create your views here.
def login(request):
    return render(request, 'tim_app/login.html')
    
def offer(request):
    if request.method == 'POST':
        ofre.add_offer(request)
        return HttpResponseRedirect(reverse('tim_app:login'))
    else:
        return render(request, 'tim_app/offer.html')

def request(request):
    if request.method == 'POST':
        ofre.add_request(request)
        return HttpResponseRedirect(reverse('tim_app:login'))
    else:
        return render(request, 'tim_app/request.html')
