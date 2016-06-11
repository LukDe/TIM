from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from tim_app.models import User, Request, Supply

#test method can be deleted in the future
def hello():
    print('test')

def delete_user(username):
    # i=0 ??
    # get object from primary key
    user = User.objects.get(username = username)
    # delete all offers with that username
    Supply.objects.get(username = user).delete()
    # delete all requests with that username
    Request.objects.get(username = user).delete()
    # delete user object
    user.delete()

    # muss noch getestet werden!!