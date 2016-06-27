from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from tim_app.models import User, Request, Supply

def create_user_phone(userName,number):

    if User.objects.filter(username=userName):
       print('username is already taken')
    else:
        #random password has to be added
        u = User(username=userName,password='123abc',phoneNr=number)
        u.save()

def create_user_complete(userName, passw, number, mail, position, rad):

    if User.objects.filter(username=userName):
        print('username is already taken')
    else:
        # random password has to be added
        u = User(username=userName, password=passw, phoneNr=number, email=mail, location=position, radius= rad)
        u.save()
