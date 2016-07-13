from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from tim_app.models import User, Request, Supply

def delete_user(username):
    # get object from primary key
    user = User.objects.get(username = username)
    # delete all offers with that username
    Supply.objects.all().filter(username = user).delete()
    # delete all requests with that username
    Request.objects.all().filter(username = user).delete()
    # deletes user
    user.delete()
