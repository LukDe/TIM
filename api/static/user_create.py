from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from tim_app.models import User, Request, Supply


def create_user(username,password):
    User.objects.get

